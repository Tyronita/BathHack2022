from typing import List
from LineModel import LineModel
from TableModel import TableModel


class NetworkModel(TableModel):
    def __init__(self, lines: List) -> None:
        self.lines = lines

    def addLine(self, line: LineModel):
        self.lines.append(line)

    def toTuple(self):
        return tuple(self.lines)

    def getLines(self) -> List:
        """Returns list of lines in the network"""
        return self.lines

    def getLineWithLineID(self, LineId) -> LineModel:
        """Returns Line with id if exists"""
        for line in self.lines:
            if line.id == LineId:
                return line
        return None

    def getLinesTuple(self) -> tuple:
        return None