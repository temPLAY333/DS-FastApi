from ...main import router, app
from ..services import ProductServieImpl
from ..controllers import BaseControllerImpl

class ProductController(BaseControllerImpl):
    def __init__(self, urlPrefix: str="/fakestoreapi.com/products") -> None:
        self.service = ProductServieImpl()
        app.include_router(router, prefix=urlPrefix)

    @router.get("/{precioMinimo}")
    def get_all(self, precioMinimo):
        try:
            return self.service.buscarPorPrecioMayorA(precioMinimo)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}
    
    @router.get("/{id}")
    def get_one(self, precioMinimo: int, precioMaximo: int):
        try:
            return self.service.buscarPorPrecioEntre(precioMinimo, precioMaximo)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}