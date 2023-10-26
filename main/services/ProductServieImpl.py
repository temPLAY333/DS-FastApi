from . import BaseServiceImpl
from ..respositories import ProductRepo

class BaseServiceImpl(BaseServiceImpl):
    def __init__(self):
        self.repository = ProductRepo()
    
    def buscarPorPrecioMayorA(self, precioMinimo) -> list|Exception:
        try:
            return self.repository.buscarPorPrecioMayorA(precioMinimo)
        except Exception as e:
            raise Exception(str(e))

    def buscarPorPrecioEntre(self, precioMinimo, precioMaximo) -> list|Exception:
        try:
            return self.repository.buscarPorPrecioEntre(precioMinimo, precioMaximo)
        except Exception as e:
            raise Exception(str(e))
