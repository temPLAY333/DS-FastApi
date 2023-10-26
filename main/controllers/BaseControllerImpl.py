from ...main import router, app
from pydantic import BaseModel
from ..entities import BaseTable
from ..services import BaseServiceImpl
from ..controllers import BaseController
class BaseControllerImplement(BaseController):
    def __init__(self, urlPrefix: str="/fakestoreapi.com") -> None:
        self.service = BaseServiceImpl()
        app.include_router(router, prefix=urlPrefix)

    @router.get("/")
    def getAll(self):
        try:
            return self.service.findAll()
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}
    
    @router.get("/{id}")
    def getOne(self, id: int):
        try:
            return self.service.findById(id)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}
        
    @router.post("/", response_model=BaseTable)
    def post(self, base: BaseModel):
        try:
            return self.service.save(base)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}

    @router.put("/{id}", response_model=BaseTable)
    def put(self, base: BaseModel, id: int):
        try:
            return self.service.update(base, id)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}

    @router.delete("/{id}")
    def delete(self, id: int):
        try:
            return self.service.delete(id)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}