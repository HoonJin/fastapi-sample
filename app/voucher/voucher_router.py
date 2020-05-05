from typing import List

from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse

from .domains import VoucherPriceDto
from .entities import Voucher
from .voucher_dao import VoucherDao
from .voucher_service import VoucherService

voucher_router = APIRouter()
voucher_service = VoucherService()


@voucher_router.post('/vouchers/crawl_by_seller/{seller_id:int}', response_model=List[VoucherPriceDto])
async def crawl(seller_id: int = Path(...)):
    result = await voucher_service.crawl(seller_id)
    return result


@voucher_router.get('/vouchers', response_model=List[Voucher])
async def get_all():
    result = await VoucherDao.get_all()
    return result
