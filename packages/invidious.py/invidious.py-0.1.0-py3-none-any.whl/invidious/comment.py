from dataclasses import dataclass, field
from typing import List

@dataclass
class Comment:
    """Comment class."""

    author: str=""
    authorId: str=""
    authorUrl: str=""
    authorThumbnails: List[dict]=field(
        default_factory=lambda: list()
    )
    
    commentId: str=""

    content: str=""
    contentHtml: str=""

    published: int=0
    publishedText: str=""

    likeCount: int=0
    isEdited: bool=False
    authorIsChannelOwner: bool=False
    verified: bool=False

    def from_json(self, data) -> None:
        """Loads class info from dictionary"""
        for key in data:
            setattr(self, key, data[key])

    def convert(self, cls):
        self.__class__ = cls
