import asyncio
import itertools
from typing import List

from config.exceptions import NotFoundException
from app.crawling.crawling_service import CrawlingService
from . import voucher_parser
from .domains import VoucherBidAskDto
from .entities import VoucherStore, Voucher
from .voucher_dao import VoucherDao
from .voucher_price_dao import VoucherPriceDao
from .voucher_store_dao import VoucherStoreDao


class VoucherService:
    async def crawl_all_store(self) -> List[VoucherBidAskDto]:
        sequence_id = await CrawlingService.generate_voucher_job_sequence()
        stores = await VoucherStoreDao.get_all()
        result = await asyncio.gather(*[self.crawl_by_store(s, sequence_id) for s in stores])
        return list(itertools.chain.from_iterable(result))

    async def crawl_by_store_id(self, store_id: int) -> List[VoucherBidAskDto]:
        store = await VoucherStoreDao.find_by_id(store_id)
        if store is None:
            raise NotFoundException
        return await self.crawl_by_store(store, 0)

    @staticmethod
    async def last_tickers():
        sequence = await CrawlingService.get_voucher_last_sequence()
        stores = await VoucherStoreDao.get_all()
        vouchers = await VoucherDao.get_all()
        prices = await VoucherPriceDao.get_by_sequence_id(sequence.id)

        def get_voucher_last_ticker(voucher: Voucher):
            def get_books(side: str):
                books = filter(lambda x: x.voucher_id == voucher.id and x.side == side, prices)
                return list(map(lambda x: {
                    'price': x.price,
                    'discount_rate': (voucher.par_value - x.price) / voucher.par_value * 100,
                    'store': next(filter(lambda y: x.store_id == y.id, stores)).name
                }, books))
            return {
                'name': voucher.name,
                'timestamp': sequence.timestamp,
                'bids': get_books('bid'),
                'asks': get_books('ask'),
            }
        return list(map(get_voucher_last_ticker, vouchers))

    @staticmethod
    async def crawl_by_store(store: VoucherStore, sequence_id: int) -> List[VoucherBidAskDto]:
        vouchers = await VoucherDao.get_all()
        crawl_result = await voucher_parser.parse_data(store)

        for data in crawl_result:
            voucher = next(filter(lambda x: x.name == data.name, vouchers))
            await VoucherPriceDao.insert(voucher.id, store.id, 'bid', data.bid, sequence_id)
            await VoucherPriceDao.insert(voucher.id, store.id, 'ask', data.ask, sequence_id)
        return crawl_result
