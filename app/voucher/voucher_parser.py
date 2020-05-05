import itertools
import logging
import re
from decimal import Decimal
from typing import Iterator, Dict, List

import aiohttp
from bs4 import BeautifulSoup, Tag

from .domains import VOUCHER_NAME_DICT
from .entites import VoucherSeller


async def parse_data(seller: VoucherSeller) -> List[Dict]:
    method_dict = {
        '우천사': __parse_wooticket_data,
        '모두티켓': __parse_modooticket_data,
        '상품권가게': __parse_ticketstore_data,
        '우현상품권': __parse_woohyun_data,
    }
    return list(filter(lambda x: x['name'] is not None, await method_dict[seller.name]()))


async def __parse_wooticket_data() -> Iterator[Dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.wooticket.com/popup_price.php') as res:
            text = await res.text()
    bs = BeautifulSoup(text, "html.parser")
    tables = bs.find_all('table')
    trs = tables[4].find_all('tr')

    tr_data = [[td.text.split() for td in tr.find_all('td')] for tr in trs]
    temp = list(map(lambda x: [{
        'name': __get_defined_name(' '.join(x[1])),
        'side': 'bid',
        'price': __parse_number(x[2][0]),
    }, {
        'name': __get_defined_name(' '.join(x[1])),
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
        'name': __get_defined_name(x.string),
        'side': 'bid',
        'price': __parse_number(x.next_element.next_element.next_element.next_element.next_element.next_element.text),
    }, {
        'name': __get_defined_name(x.string),
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
        if "헌거" not in raw_name and __get_defined_name(raw_name.split('/')[0].strip()) is not None:
            filtered.append(row)

    def get_data(bs_tag: Tag) -> List[Dict]:
        tds = bs_tag.find_all('td')
        name = __get_defined_name(tds[2].text.split('/')[0].strip())
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


async def __parse_woohyun_data() -> Iterator[Dict]:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async def get_lis(url: str):
            async with session.get(url) as res:
                text = await res.text()
                bs = BeautifulSoup(text, 'html.parser')
                return bs.find_all('li', class_='sct_li')

        # todo 현재는 상품권만 읽어오는데 할인마트등의 카테고리에서도 읽어오고 중복데이터는 걸러내서 저장해야함.
        # 백화점 & 할인마트 & 금강제화
        lis1 = await get_lis('https://wooh.co.kr/shop/list.php?ca_id=10')
        # trs2 = await get_lis('https://wooh.co.kr/shop/list.php?ca_id=20&sort=&sortodr=&page=2')
        # # 주유
        # trs3 = await get_lis('https://wooh.co.kr/shop/list.php?ca_id=30')
        # # 도서문화
        # trs4 = get_lis('https://wooh.co.kr/shop/list.php?ca_id=50')
        # # 기프트카드
        # trs5 = get_lis('https://wooh.co.kr/shop/list.php?ca_id=60')

    def get_data(bs_tag: Tag) -> List[Dict]:
        name = __get_defined_name(bs_tag.find('div', class_='sct_txt').text.strip())
        prices = list(map(lambda x: x.text, bs_tag.find_all('b')))
        return [{
            'name': name,
            'side': 'bid',
            'price': __parse_number(prices[0])
        }, {
            'name': name,
            'side': 'ask',
            'price': __parse_number(prices[1])
        }]
    return itertools.chain.from_iterable(list(map(get_data, lis1)))


def __get_defined_name(element: str) -> str:
    name = VOUCHER_NAME_DICT.get(element)
    if name is None:
        logging.warning(f'unknown voucher name: {element}')
    return name


def __parse_number(text: str) -> Decimal:
    return Decimal(''.join([t for t in text if t.isdigit()]))
