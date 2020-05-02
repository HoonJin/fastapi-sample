import itertools
import re
from decimal import Decimal
from typing import Iterator, Dict, List

import aiohttp
from bs4 import BeautifulSoup, Tag

from .domains import VOUCHER_NAME_DICT
from .entites import VoucherSeller


async def parse_data(seller: VoucherSeller) -> Iterator[Dict]:
    method_dict = {
        '우천사': __parse_wooticket_data,
        '모두티켓': __parse_modooticket_data,
        '상품권가게': __parse_ticketstore_data
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
        'price': __parse_number(x[2][0]),
    }, {
        'name': VOUCHER_NAME_DICT.get(' '.join(x[1]), ' '.join(x[1])),
        'side': 'ask',
        'price': __parse_number(x[3][0])
    }], tr_data[1:]))
    return itertools.chain.from_iterable(temp)


async def __parse_modooticket_data() -> Iterator[Dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.modooticket.co.kr/shop/main/index.php') as res:
            text = await res.text()
    bs = BeautifulSoup(text, "html.parser")
    rows = bs.find_all(href=re.compile("/goods/goods_view.php?"))

    filtered = [rows[x] for x in range(0, len(rows), 4)]
    temp = list(map(lambda x: [{
        'name': VOUCHER_NAME_DICT.get(x.string, x.string),
        'side': 'bid',
        'price': __parse_number(x.next_element.next_element.next_element.next_element.next_element.next_element.text),
    }, {
        'name': VOUCHER_NAME_DICT.get(x.string, x.string),
        'side': 'ask',
        'price': __parse_number(x.next_element.next_element.next_element.next_element.next_element.next_element
                                .next_element.next_element.next_element.next_element.next_element.next_element
                                .next_element.next_element.next_element.next_element.next_element.next_element.text)
    }], filtered))
    return itertools.chain.from_iterable(temp)


async def __parse_ticketstore_data() -> Iterator[Dict]:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async with session.get('https://www.ticketstore.co.kr/shop/purchase_list.php') as res:
            text = await res.text()
    bs = BeautifulSoup(text, 'html.parser')
    trs = bs.find_all('tr')
    rows = list(filter(lambda x: x['class'][0] != 'list-head', trs))

    filtered = []
    # 헌거 를 걸러낸 뒤에 다시 작업을 해야해서 lambda를 사용하지 않음
    for row in rows:
        raw_name = row.find_all('td')[2].text
        if "헌거" not in raw_name and VOUCHER_NAME_DICT.get(raw_name.split('/')[0].strip()) is not None:
            filtered.append(row)

    def get_data(bs_tag: Tag) -> List[Dict]:
        tds = bs_tag.find_all('td')
        name = VOUCHER_NAME_DICT.get(tds[2].text.split('/')[0].strip())
        return [{
            'name': name,
            'side': 'bid',
            'price': __parse_number(tds[3].find('font').text)
        }, {
            'name': name,
            'side': 'ask',
            'price': __parse_number(tds[4].find('font').text)
        }]
    return itertools.chain.from_iterable(list(map(get_data, filtered)))


def __parse_number(text: str) -> Decimal:
    return Decimal(''.join([t for t in text if t.isdigit()]))
