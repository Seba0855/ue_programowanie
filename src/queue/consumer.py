from typing import Callable

from src.model.job import Job, JobStatus
from src.queue.common import get_next_pending_job, update_job

## TODO: REFACTOR

def start_consumer(task: Callable[[Job], str]) -> None:
    while True:
        if (job := get_next_pending_job()) is not None:
            job.status = JobStatus.IN_PROGRESS
            update_job(job)

            result = task(job)
            job.result = result

            job.status = JobStatus.FINISHED
            update_job(job)