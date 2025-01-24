from dataclasses import dataclass
from enum import StrEnum

from src.model.InputType import InputType


class WorkerStatus(StrEnum):
    WAITING = "waiting"
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"


@dataclass
class Work:
    CSV_HEADER = ["work_id", "input_type", "status", "found_people", "image_source"]

    work_id: int
    input_type: InputType
    source: str
    work_status: WorkerStatus = WorkerStatus.WAITING
    found_people: str = ""

    def to_csv(self) -> list[str]:
        return list(map(str, [self.work_id, self.input_type, self.work_status, self.found_people, self.source]))

    @staticmethod
    def from_csv(iterable: list[str]) -> "Work":
        assert len(iterable) == len(Work.CSV_HEADER)
        return Work(
            work_id=int(iterable[0]),
            input_type=InputType(iterable[1]),
            work_status=WorkerStatus(iterable[2]),
            found_people=iterable[3],
            source=iterable[4]
        )
