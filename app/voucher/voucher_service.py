import itertools
from decimal import Decimal

import aiohttp
from bs4 import BeautifulSoup

from config.exceptions import NotFoundException
from database import db
from .domains import VOUCHER_NAME_DICT
from .voucher_dao import VoucherDao
from .voucher_price_dao import VoucherPriceDao
from .voucher_seller_dao import VoucherSellerDao


class VoucherService:

    @staticmethod
    async def crawl(seller_id: int):
        seller = await VoucherSellerDao.find_by_id(seller_id)
        if seller is None:
            raise NotFoundException

        vouchers = await VoucherDao.get_all()

        async with aiohttp.ClientSession() as session:
            async with session.get(seller.url) as res:
                text = await res.text(encoding='euc-kr')
        bs = BeautifulSoup(text, "html.parser")
        tables = bs.find_all('table')
        trs = tables[4].find_all('tr')

        tr_data = [[td.text.split() for td in tr.find_all('td')] for tr in trs]
        prepared = list(map(lambda x: [{
            'name': VOUCHER_NAME_DICT.get(' '.join(x[1]), ' '.join(x[1])),
            'side': 'bid',
            'price': Decimal(x[2][0].replace(',', '')),
        }, {
            'name': VOUCHER_NAME_DICT.get(' '.join(x[1]), ' '.join(x[1])),
            'side': 'ask',
            'price': Decimal(x[3][0].replace(',', ''))
        }], tr_data[1:]))

        async with db.transaction():
            for data in itertools.chain.from_iterable(prepared):
                voucher = next(filter(lambda x: x.name == data['name'], vouchers))
                await VoucherPriceDao.insert(voucher.id, seller_id, data['side'], data['price'])
        return


