import asyncio

import aiohttp
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import conf

__HOST = conf.get('HOST')


async def crawl_voucher():
    print(__HOST)
    # async with aiohttp.ClientSession() as session:
    #     async with session.post(f'{__HOST}/crawl_by_store_id') as res:
    #         await res.text()


async def get_scheduler():
    scheduler = AsyncIOScheduler()
    # scheduler.add_job(crawl_voucher, 'cron', minute='*/20', second='10')
    scheduler.add_job(crawl_voucher, 'cron', minute='*', second='*/2')
    scheduler.start()

if __name__ == '__main__':
    asyncio.gather(get_scheduler())
    asyncio.get_event_loop().run_forever()
