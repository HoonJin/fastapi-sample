from config.exceptions import NotFoundException
from database import db
from . import voucher_parser
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
        crawl_result = await voucher_parser.parse_data(seller)

        async with db.transaction():
            for data in crawl_result:
                voucher = next(filter(lambda x: x.name == data['name'], vouchers))
                await VoucherPriceDao.insert(voucher.id, seller_id, data['side'], data['price'])
        return


