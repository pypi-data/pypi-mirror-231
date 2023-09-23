from dataclasses import dataclass, field
from typing import List

@dataclass
class PlaylistItem:
    """PlaylistItem class. Used in search."""

    title: str=""
    playlistId: str=""
    author: str=""
    authorId: str=""
    authorUrl: str=""
    videoCount: int=0

    videos: List[dict]=field(
        default_factory=lambda: list()
    )

    def from_json(self, data) -> None:
        """Loads class info from dictionary"""
        for key in data:
            setattr(self, key, data[key])

    def convert(self, cls):
        self.__class__ = cls


