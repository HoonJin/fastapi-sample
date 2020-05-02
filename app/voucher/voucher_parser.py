import itertools
from decimal import Decimal
from typing import Iterator, Dict

import aiohttp
from bs4 import BeautifulSoup

from .domains import VOUCHER_NAME_DICT
from .entites import VoucherSeller


async def parse_data(seller: VoucherSeller) -> Iterator[Dict]:
    method_dict = {
        '우천사': __parse_wooticket_data
    }
    return await method_dict[seller.name]()


async def __parse_wooticket_data() -> Iterator[Dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.wooticket.com/popup_price.php') as res:
            text = await res.text()
    bs = BeautifulSoup(text, "html.parser")
    tables = bs.find_all('table')
    trs = tables[4].find_all('tr')

    tr_data = [[td.text.split() for td in tr.find_all('td')] for tr in trs]
    temp = list(map(lambda x: [{
        'name': VOUCHER_NAME_DICT.get(' '.join(x[1]), ' '.join(x[1])),
        'side': 'bid',
        'price': Decimal(x[2][0].replace(',', '')),
    }, {
        'name': VOUCHER_NAME_DICT.get(' '.join(x[1]), ' '.join(x[1])),
        'side': 'ask',
        'price': Decimal(x[3][0].replace(',', ''))
    }], tr_data[1:]))
    return itertools.chain.from_iterable(temp)
