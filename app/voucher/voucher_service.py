import asyncio
import itertools
from typing import List

from config.exceptions import NotFoundException
from . import voucher_parser
from .domains import VoucherPriceDto
from .entities import VoucherStore
from .voucher_dao import VoucherDao
from .voucher_price_dao import VoucherPriceDao
from .voucher_store_dao import VoucherStoreDao


class VoucherService:
    async def crawl_all_store(self) -> List[VoucherPriceDto]:
        stores = await VoucherStoreDao.get_all()
        result = await asyncio.gather(*[self.crawl_by_store(s) for s in stores])
        return list(itertools.chain.from_iterable(result))

    async def crawl_by_store_id(self, store_id: int) -> List[VoucherPriceDto]:
        store = await VoucherStoreDao.find_by_id(store_id)
        if store is None:
            raise NotFoundException
        return await self.crawl_by_store(store)

    @staticmethod
    async def crawl_by_store(store: VoucherStore) -> List[VoucherPriceDto]:
        vouchers = await VoucherDao.get_all()
        crawl_result = await voucher_parser.parse_data(store)

        for data in crawl_result:
            voucher = next(filter(lambda x: x.name == data.name, vouchers))
            await VoucherPriceDao.insert(voucher.id, store.id, 'bid', data.bid)
            await VoucherPriceDao.insert(voucher.id, store.id, 'ask', data.ask)
        return crawl_result
