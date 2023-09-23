from dataclasses import dataclass, field
from typing import List

@dataclass
class ShortVideo:
    """ShortVideo class. Used in popular videos."""

    title: str=""
    videoId: str=""
    author: str=""
    authorId: str=""
    authorUrl: str=""
    
    lengthSeconds: int=0

    viewCount: int=0
    viewCountText: str=""

    published: int=0
    publishedText: str=""

    videoThumbnails: List[dict]=field(
        default_factory=lambda: list()
    )

    def from_json(self, data) -> None:
        """Loads class info from dictionary"""
        for key in data:
            setattr(self, key, data[key])

    def convert(self, cls):
        self.__class__ = cls


