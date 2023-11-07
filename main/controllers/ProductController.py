from main import router, app
from main.services import ProductServiceImpl
from main.controllers import BaseControllerImplement

urlPrefix: str="/fakestoreapi.com/products"
service = ProductServiceImpl()

class ProductController(BaseControllerImplement):

    @router.get("/{precioMinimo}")
    def get_all(precioMinimo: int):
        try:
            return service.buscarPorPrecioMayorA(precioMinimo)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}
    
    @router.get("/{id}")
    def get_one(precioMinimo: int, precioMaximo: int):
        try:
            return service.buscarPorPrecioEntre(precioMinimo, precioMaximo)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}
        
app.include_router(router, prefix=urlPrefix)