"""

"""

from dataclasses import dataclass
from typing import Optional, List, Any


@dataclass
class Pipeline:
    """A simple pipeline; to group and stack methods together."""

    def __init__(self, stages: Optional[List[Any]] = None) -> None:
        self.stages = stages

    def run(self, dataset: Optional["Dataset"] = None) -> None:
        pass