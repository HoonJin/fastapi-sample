from enum import Enum


class CrawlingJobName(str, Enum):
    voucher = 'voucher'
    currency = 'currency'
    coin = 'coin'
