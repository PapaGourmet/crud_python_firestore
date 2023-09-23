from abc import ABC, abstractmethod
from typing import Any, List, TypeVar

T = TypeVar('T')


class IRepository(ABC):

    @abstractmethod
    def conn(self):
        pass

    @abstractmethod
    def getAll(self, collectionName: str) -> List[Any]:
        pass

    @abstractmethod
    def getByID(self, collectionName: str, documentId: str) -> Any:
        pass

    @abstractmethod
    def add(self, collectionName: str, document: T, documentId=None) -> None:
        pass

    @abstractmethod
    def deleteByDocumentId(self, collectionName: str, documentId: str) -> None:
        pass

    @abstractmethod
    def updateByDocumentId(self, collectionName, documentId, data) -> None:
        pass
