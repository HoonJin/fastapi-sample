from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse

from .voucher_service import VoucherService

voucher_router = APIRouter()
voucher_service = VoucherService()


@voucher_router.post('/voucher/crawl_by_seller/{seller_id:int}')
async def crawl(seller_id: int = Path(...)):
    await voucher_service.crawl(seller_id)
    return JSONResponse({})
