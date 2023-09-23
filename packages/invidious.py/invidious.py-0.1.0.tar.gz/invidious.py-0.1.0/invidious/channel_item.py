from dataclasses import dataclass, field
from typing import List

@dataclass
class ChannelItem:
    """ChannelItem class. Used in search."""

    author: str=""
    authorId: str=""
    authorUrl: str=""
    authorThumbnails: List[dict]=field(
        default_factory=lambda: list()
    )

    subCount: int=0
    videoCount: int=0

    description: str=""
    descriptionHtml: str=""

    def from_json(self, data) -> None:
        """Loads class info from dictionary"""
        for key in data:
            setattr(self, key, data[key])

    def convert(self, cls):
        self.__class__ = cls


