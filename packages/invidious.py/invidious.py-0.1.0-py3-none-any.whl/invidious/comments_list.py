from dataclasses import dataclass, field
from typing import List

@dataclass
class CommentsList:
    """Comments list class."""

    videoId: str=""
    commentCount: int=0
    continuation: str=""

    comments: List[dict]=field(
        default_factory=lambda: list()
    )

    def from_json(self, data) -> None:
        """Loads class info from dictionary"""
        for key in data:
            setattr(self, key, data[key])

    def convert(self, cls):
        self.__class__ = cls
