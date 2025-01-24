from tempfile import NamedTemporaryFile
from typing import Callable
from pathlib import Path
import csv
import os

from src.model.work import Work, WorkerStatus
from src.util.constants import WORK_DB_FILE_NAME


def work_lookup(predicate: Callable[[Work], bool]) -> Work | None:
    path = Path(WORK_DB_FILE_NAME)
    if path.exists():
        with open(path, 'r') as f:
            reader = csv.reader(f)

            for i, line in enumerate(reader):
                # Skipping the header
                if i == 0:
                    continue

                work = Work.from_csv(line)
                if predicate(work):
                    return work

    return None


def find_work_by_id(id: int) -> Work | None:
    return work_lookup(lambda work: work.work_id == id)


def get_next_waiting_work() -> Work | None:
    return work_lookup(lambda work: work.work_status == WorkerStatus.WAITING)


def update_work(job: Work) -> None:
    temp_path = ""
    with NamedTemporaryFile('w', newline='', delete=False) as temp:
        temp_path = temp.name
        writer = csv.writer(temp)

        with open(WORK_DB_FILE_NAME, 'r') as f:
            reader = csv.reader(f)

            for i, line in enumerate(reader):
                if i == 0:
                    # Write CSV header
                    writer.writerow(line)
                    continue

                old_job = Work.from_csv(line)
                if old_job.work_id == job.work_id:
                    old_job = job

                writer.writerow(old_job.to_csv())

    if temp_path != "":
        # Replace temp file with original
        os.replace(temp_path, WORK_DB_FILE_NAME)
