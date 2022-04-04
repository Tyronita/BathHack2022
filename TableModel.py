from abc import ABC, abstractmethod

class TableModel():

    @abstractmethod
    def toTuple(self):
        pass
