from typing import List

from fastapi import APIRouter, Path

from .domains import VoucherPriceDto
from .entities import Voucher
from .voucher_dao import VoucherDao
from .voucher_service import VoucherService

voucher_router = APIRouter()
voucher_service = VoucherService()


@voucher_router.post('/vouchers/crawl', response_model=List[VoucherPriceDto])
async def crawl():
    result = await voucher_service.crawl_all_store()
    return result


@voucher_router.post('/vouchers/crawl_by_seller/{store_id:int}', response_model=List[VoucherPriceDto])
async def crawl(store_id: int = Path(...)):
    result = await voucher_service.crawl_by_store_id(store_id)
    return result


@voucher_router.get('/vouchers', response_model=List[Voucher])
async def get_all():
    result = await VoucherDao.get_all()
    return result
