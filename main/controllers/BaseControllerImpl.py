from main import router, app
from pydantic import BaseModel
from main.services import BaseServiceImpl
from main.controllers import BaseController
import json

service = BaseServiceImpl()

class BaseControllerImplement(BaseController):

    @router.get("")
    def getAll():
        try:
            print(json.dumps(service.findAll()))
            return json.dumps(service.findAll())
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."+ str(e.args)}
    
    @router.get("/{id}")
    def getOne(id: int):
        try:
            return service.findById(id)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}
        
    @router.post("", response_model=BaseModel)
    def post(base: BaseModel):
        try:
            return service.save(base)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}

    @router.put("/{id}", response_model=BaseModel)
    def put(base: BaseModel, id: int):
        try:
            return service.update(base, id)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}

    @router.delete("/{id}")
    def delete(id: int):
        try:
            return service.delete(id)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}