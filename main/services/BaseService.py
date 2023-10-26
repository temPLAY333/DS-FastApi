from abc import ABCMeta, abstractmethod

class BaseService(metaclass=ABCMeta):

    @abstractmethod
    def findAll(self) -> list|Exception:
        pass

    @abstractmethod
    def findById(self, id) -> list|Exception:
        pass

    @abstractmethod
    def save(self, entity) -> list|Exception:
        pass

    @abstractmethod
    def update(self, entity, id) -> list|Exception:
        pass

    @abstractmethod
    def delete(self, id) -> list|Exception:
        pass