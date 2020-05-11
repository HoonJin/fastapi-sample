from .crawling_sequence_dao import CrawlingSequenceDao


class CrawlingService:
    @staticmethod
    async def generate_voucher_job_sequence():
        return await CrawlingSequenceDao.insert('voucher')

    @staticmethod
    async def get_voucher_last_sequence():
        return await CrawlingSequenceDao.get_last_by_job_name('voucher')
