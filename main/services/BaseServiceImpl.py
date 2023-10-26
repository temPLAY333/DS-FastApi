from . import BaseService
from ..entities import BaseRepo

class BaseServiceImpl(BaseService):
    def __init__(self):
        self.repository = BaseRepo()

    def findAll(self):
        try:
            return self.repository.findAll()
        except Exception as e:
            raise Exception(str(e))

    def findById(self, id):
        try:
            return self.repository.findById(id)
        except Exception as e:
            raise Exception(str(e))

    def save(self, entity):
        try:
            return self.repository.save(entity)
        except Exception as e:
            raise Exception(str(e))

    def update(self, entity, id):
        try:
            optEntity = self.repository.findById(id)
            if optEntity:
                entityUpdate = self.repository.save(entity)
                return entityUpdate
        except Exception as e:
            raise Exception(str(e))

    def delete(self, id):
        try:
            if self.repository.findById(id):
                self.repository.delete(id)
                return True
            else:
                raise Exception()
        except Exception as e:
            raise Exception(str(e))