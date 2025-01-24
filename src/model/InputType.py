from dataclasses import dataclass
from enum import StrEnum

class InputType(StrEnum):
    PATH = "PATH"
    URL = "URL"
    BASE64 = "BASE64"