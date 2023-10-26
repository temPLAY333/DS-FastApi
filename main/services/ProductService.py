from abc import ABCMeta, abstractmethod
from . import BaseService

class ProductService(BaseService, metaclass=ABCMeta):
    @abstractmethod
    def buscarPorPrecioMayorA(self) -> list|Exception:
        pass

    @abstractmethod
    def buscarPorPrecioEntre(self, id) -> list|Exception:
        pass