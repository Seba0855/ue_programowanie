from pathlib import Path
import csv

from src.model.work import Work, InputType
from src.util.constants import JOBS_FILE_NAME

## TODO: REFACTOR

def enqueue_job(job_type: InputType, content: str) -> Work:
    csv_path = Path(JOBS_FILE_NAME)
    write_header = not csv_path.exists()

    with open(csv_path, "a+", newline='') as f:
        reader = csv.reader(f)
        writer = csv.writer(f)
        f.seek(0)  # required for reader in a+ file mode

        if write_header:
            writer.writerow(Work.FIELD_NAMES)

        lines = [line for line in reader]

        job_id = 0
        if reader.line_num > 1:
            last_job = Work.from_csv(lines[-1])
            job_id = last_job.id + 1

        job = Work(job_id, job_type, content)
        writer.writerow(job.to_csv())

        print(f"Successfully enqueued a new job with id={job_id}")
        return job
