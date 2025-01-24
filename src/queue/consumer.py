from typing import Callable

from src.model.work import Work, WorkerStatus
from src.queue.common import get_next_waiting_work, update_work

## TODO: REFACTOR

def start_consumer(task: Callable[[Work], str]) -> None:
    print("Consumer started")
    while True:
        if (work := get_next_waiting_work()) is not None:
            print(f"found job that is not none: ${work}")
            work.status = WorkerStatus.IN_PROGRESS
            update_work(work)
            print("updating job")

            result = task(work)
            print("result: ", result)
            work.result = result

            work.status = WorkerStatus.FINISHED
            print("job finished")
            update_work(work)