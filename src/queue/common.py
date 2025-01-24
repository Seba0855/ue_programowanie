from tempfile import NamedTemporaryFile
from typing import Callable
from pathlib import Path
import csv
import os

from src.model.work import Work, WorkerStatus
from src.util.constants import JOBS_FILE_NAME

## TODO: REFACTOR ALL

def work_lookup(predicate: Callable[[Work], bool]) -> Work | None:
    path = Path(JOBS_FILE_NAME)
    if path.exists():
        with open(path, 'r') as f:
            reader = csv.reader(f)

            for i, line in enumerate(reader):
                if i == 0:
                    continue  # skip header

                job = Work.from_csv(line)
                if predicate(job):
                    print("found job")
                    return job

    return None


def find_work_by_id(job_id: int) -> Work | None:
    return work_lookup(lambda job: job.id == job_id)


def get_next_waiting_work() -> Work | None:
    return work_lookup(lambda work: work.status == WorkerStatus.WAITING)


def update_work(job: Work) -> None:
    temp_file_path = ""
    with NamedTemporaryFile('w', newline='', delete=False) as temp:
        temp_file_path = temp.name
        writer = csv.writer(temp)

        with open(JOBS_FILE_NAME, 'r') as f:
            reader = csv.reader(f)

            for i, line in enumerate(reader):
                if i == 0:
                    writer.writerow(line)  # write header
                    continue

                old_job = Work.from_csv(line)
                if old_job.id == job.id:
                    old_job = job

                writer.writerow(old_job.to_csv())

    if temp_file_path != "":
        # replace temporary file with original
        os.replace(temp_file_path, JOBS_FILE_NAME)