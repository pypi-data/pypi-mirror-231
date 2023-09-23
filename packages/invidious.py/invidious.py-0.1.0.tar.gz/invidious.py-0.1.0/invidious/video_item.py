from dataclasses import dataclass, field
from typing import List

@dataclass
class VideoItem:
    """VideoItem class. Used in search."""

    title: str=""
    videoId: str=""
    author: str=""
    authorId: str=""
    authorUrl: str=""
   
    description: str=""
    descriptionHtml: str=""

    lengthSeconds: int=0
    viewCount: int=0
    published: int=0
    publishedText: str=""

    genre: str=""
    genreUrl: str=""

    premium: bool=False
    liveNow: bool=False
    isUpcoming: bool=False

    videoThumbnails: List[dict]=field(
        default_factory=lambda: list()
    )

    def from_json(self, data) -> None:
        """Loads class info from dictionary"""
        for key in data:
            setattr(self, key, data[key])

    def convert(self, cls):
        self.__class__ = cls


