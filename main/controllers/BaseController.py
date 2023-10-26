from abc import ABCMeta, abstractmethod

class BaseController(metaclass=ABCMeta):

    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def getOne(self, id):
        pass

    @abstractmethod
    def post(self, object):
        pass

    @abstractmethod
    def put(self, object, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass