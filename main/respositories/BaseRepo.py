from abc import ABCMeta
from ..entities import BaseTable

class BaseRepo(BaseTable, metaclass=ABCMeta):
    pass