from dataclasses import dataclass
from enum import StrEnum

from src.model.InputType import InputType

## TODO: REFACTOR

class JobStatus(StrEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"

## TODO: REFACTOR

@dataclass
class Job:
    FIELD_NAMES = ["id", "status", "type", "content", "result"]
    FIELD_COUNT = len(FIELD_NAMES)

    id: int
    type: InputType
    content: str
    status: JobStatus = JobStatus.PENDING
    result: str = ""

    @staticmethod
    def from_csv(iterable: list[str]) -> "Job":
        assert len(iterable) == Job.FIELD_COUNT
        return Job(int(iterable[0]), InputType(iterable[2]), iterable[3],  JobStatus(iterable[1]), iterable[4])

    def to_csv(self) -> list[str]:
        return list(map(str, [self.id, self.status, self.type, self.content, self.result]))