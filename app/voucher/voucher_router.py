from typing import List

from fastapi import APIRouter, Path

from .domains import VoucherBidAskDto
from .entities import Voucher
from .voucher_dao import VoucherDao
from .voucher_service import VoucherService

voucher_router = APIRouter()
voucher_service = VoucherService()


@voucher_router.post('/vouchers/crawl', response_model=List[VoucherBidAskDto])
async def crawl():
    result = await voucher_service.crawl_all_store()
    return result


@voucher_router.get('/vouchers', response_model=List[Voucher])
async def get_all():
    result = await VoucherDao.get_all()
    return result


@voucher_router.get('/vouchers/tickers')
async def get_voucher_tickers():
    result = await voucher_service.last_tickers()
    return result
