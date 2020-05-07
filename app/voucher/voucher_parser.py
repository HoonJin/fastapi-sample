import asyncio
import itertools
import logging
import re
from decimal import Decimal
from typing import Iterator, List

import aiohttp
from bs4 import BeautifulSoup, element

from .domains import VOUCHER_NAME_DICT, VoucherBidAskDto
from .entities import VoucherStore


async def parse_data(store: VoucherStore) -> List[VoucherBidAskDto]:
    method_dict = {
        '우천사': __parse_wooticket_data,
        '모두티켓': __parse_modooticket_data,
        '상품권가게': __parse_ticketstore_data,
        '우현상품권': __parse_woohyun_data,
    }
    return list(filter(lambda x: x.name is not None, await method_dict[store.name](store.name)))


async def __parse_wooticket_data(store: str) -> Iterator[VoucherBidAskDto]:
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.wooticket.com/popup_price.php') as res:
            text = await res.text()
    bs = BeautifulSoup(text, "html.parser")
    tables = bs.find_all('table')
    trs = tables[4].find_all('tr')

    tr_data = [[td.text.split() for td in tr.find_all('td')] for tr in trs]
    return map(lambda x: VoucherBidAskDto(name=__get_defined_name(' '.join(x[1])), store=store,
                                          bid=__parse_price(x[2][0]), ask=__parse_price(x[3][0])), tr_data[1:])


async def __parse_modooticket_data(store: str) -> Iterator[VoucherBidAskDto]:
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.modooticket.co.kr/shop/main/index.php') as res:
            text = await res.text()
    bs = BeautifulSoup(text, "html.parser")
    rows = bs.find_all(href=re.compile("/goods/goods_view.php?"))

    filtered = [rows[x] for x in range(0, len(rows), 4)]
    return map(lambda x: VoucherBidAskDto(
        name=__get_defined_name(x.string), store=store,
        bid=__parse_price(x.next_element.next_element.next_element.next_element.next_element.next_element.text),
        ask=__parse_price(x.next_element.next_element.next_element.next_element.next_element.next_element
                          .next_element.next_element.next_element.next_element.next_element.next_element
                          .next_element.next_element.next_element.next_element.next_element.next_element.text)
    ), filtered)


async def __parse_ticketstore_data(store: str) -> Iterator[VoucherBidAskDto]:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async with session.get('https://www.ticketstore.co.kr/shop/purchase_list.php') as res:
            text = await res.text()
    bs = BeautifulSoup(text, 'html.parser')
    trs = bs.find_all('tr')
    rows = filter(lambda x: x['class'][0] != 'list-head', trs)

    filtered = []
    # 헌거 를 걸러낸 뒤에 다시 작업을 해야해서 lambda를 사용하지 않음
    for row in rows:
        raw_name = row.find_all('td')[2].text
        if "헌거" not in raw_name and __get_defined_name(raw_name.split('/')[0].strip()) is not None:
            filtered.append(row)

    def get_data(bs_tag: element.Tag) -> VoucherBidAskDto:
        tds = bs_tag.find_all('td')
        return VoucherBidAskDto(name=__get_defined_name(tds[2].text.split('/')[0].strip()), store=store,
                                bid=__parse_price(tds[3].find('font').text), ask=__parse_price(tds[4].find('font').text)
                                )
    return map(get_data, filtered)


async def __parse_woohyun_data(store: str) -> Iterator[VoucherBidAskDto]:
    urls = [
        'https://wooh.co.kr/shop/list.php?ca_id=10',
        'https://wooh.co.kr/shop/list.php?ca_id=20&sort=&sortodr=&page=2',
        'https://wooh.co.kr/shop/list.php?ca_id=30', 'https://wooh.co.kr/shop/list.php?ca_id=50',
        'https://wooh.co.kr/shop/list.php?ca_id=60', 'https://wooh.co.kr/shop/list.php?ca_id=70',
        'https://wooh.co.kr/shop/list.php?ca_id=80',
    ]
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async def get_data(url: str) -> Iterator[VoucherBidAskDto]:
            async with session.get(url) as res:
                text = await res.text()
                bs = BeautifulSoup(text, 'html.parser')

                def __get_data(tag: element.Tag) -> VoucherBidAskDto:
                    name = __get_defined_name(tag.find('div', class_='sct_txt').text.strip())
                    prices = list(map(lambda x: x.text, tag.find_all('b')))
                    return VoucherBidAskDto(name=name, store=store,
                                            bid=__parse_price(prices[1]), ask=__parse_price(prices[0]))
                return map(__get_data, bs.find_all('li', class_='sct_li'))

        temp = list(itertools.chain.from_iterable(await asyncio.gather(*[get_data(url) for url in urls])))
    name_set = set([t.name for t in temp])
    return map(lambda name: next(filter(lambda ele: ele.name == name, temp)), name_set)


def __get_defined_name(ele: str) -> str:
    name = VOUCHER_NAME_DICT.get(ele)
    if name is None:
        logging.warning(f'unknown voucher name: {ele}')
    return name


def __parse_price(text: str) -> Decimal:
    return Decimal(''.join([t for t in text if t.isdigit()]))
