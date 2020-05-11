from app import AbstractBaseModel
from .domains import CrawlingJobName


class CrawlingSequence(AbstractBaseModel):
    job_name: CrawlingJobName
    timestamp: int

    class Config:
        orm_mode = True
