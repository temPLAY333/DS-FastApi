from main import app
from ..services import ProductServieImpl
from ..controllers import BaseControllerImpl

class ProductController(BaseControllerImpl):
    def __init__(self) -> None:
        self.service = ProductServieImpl()

    @app.get("/productos/{precioMinimo}")
    def get_all(self, precioMinimo):
        try:
            return self.service.buscarPorPrecioMayorA(precioMinimo)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}
    
    @app.get("/{id}")
    def get_one(self, precioMinimo: int, precioMaximo: int):
        try:
            return self.service.buscarPorPrecioEntre(precioMinimo, precioMaximo)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}