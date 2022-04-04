from typing import List
from TableModel import TableModel


class LineModel(TableModel):
    def __init__(self, id, name, status, colour) -> None:
        self.id = id
        self.name = name            # name of the line
        self.status = status        # boolean representing if the line is closed
        self.colour = colour        # colour of line in rgb format
        self.stations = []          # list of stations on line in order

    def __repr__(self) -> str:
        return self.toTuple().__str__()

    def getId(self) -> int:
        return self.id

    def getName(self) -> str:
        return self.name

    def getStatus(self) -> int:
        return self.status

    def getStatusColour(self) -> str:
        if (self.status == 0):
            return "#b52424"
        else:
            return "#36b325"

    def getColour(self) -> str:
        return self.colour
    
    def getRoute(self) -> str:
        return self.stations[0].name+" - "+self.stations[-1].name

    def getStartRoute(self) -> str:
        return self.stations[0].name

    def getEndRoute(self) -> str:
        return self.stations[-1].name

    def getNumStations(self) -> int:
        """Returns the number of stations"""
        return len(self.stations)

    def toTuple(self) -> tuple:
        """Returns tuple of values in order of columns in database"""
        return (self.id, self.name, self.status, self.colour)

    def getStations(self) -> List:
        """Returns stations on route in order"""
        return self.stations