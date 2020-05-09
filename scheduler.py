import asyncio
import logging
from datetime import datetime

import aiohttp
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import conf

__HOST = conf.get('HOST')
logging.basicConfig(level=logging.INFO)


async def log():
    now = datetime.utcnow()
    logging.info(f'scheduler is active at {now}')


async def crawl_vouchers():
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{__HOST}/vouchers/crawl') as res:
            await res.text()


async def get_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(log, 'cron', minute='0/5')
    scheduler.add_job(crawl_vouchers, 'cron', hour='1/4', minute='10', second='1')
    scheduler.start()

if __name__ == '__main__':
    logging.info(f'start viole scheduler with host: {__HOST} at {datetime.utcnow()}')
    asyncio.gather(get_scheduler())
    asyncio.get_event_loop().run_forever()
