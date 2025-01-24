from dataclasses import dataclass
from enum import StrEnum

from src.model.InputType import InputType

class WorkerStatus(StrEnum):
    WAITING = "waiting"
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"

@dataclass
class Work:
    FIELD_NAMES = ["id", "status", "type", "content", "result"]
    FIELD_COUNT = len(FIELD_NAMES)

    id: int
    type: InputType
    content: str
    status: WorkerStatus = WorkerStatus.WAITING
    result: str = ""

    @staticmethod
    def from_csv(iterable: list[str]) -> "Work":
        assert len(iterable) == Work.FIELD_COUNT
        return Work(int(iterable[0]), InputType(iterable[2]), iterable[3], WorkerStatus(iterable[1]), iterable[4])

    def to_csv(self) -> list[str]:
        return list(map(str, [self.id, self.status, self.type, self.content, self.result]))