from dataclasses import dataclass
from typing import List, Optional

from tables import csv_sep


class MetadataBlock(dict):

    def __init__(self, origin: Optional[str] = None):
        super().__init__()
        self.origin = origin

    def __repr__(self):
        sep = csv_sep()
        return "\n".join(f"{k}:{sep}{self[k]}{sep}" for k in self)


@dataclass
class Directive:

    name: str
    lines: List[str]
    origin: Optional[str] = None

    def __repr__(self):
        return f"***{self.name}{csv_sep()}\n" + "\n".join(self.lines)

