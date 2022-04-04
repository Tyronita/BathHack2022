from TableModel import TableModel


class StationModel(TableModel):
    def __init__(self, id, name, numOfCameras, prevalence, works, status) -> None:
        self.id = id
        self.name = name                    # name of the station
        self.numOfCameras = numOfCameras    # num of cameras at the station
        self.prevalence = prevalence        # how busy is the station in a score out of 10
        self.works = works                  # boolean if work is being done at the station
        self.status = status                # boolean representing if the station is closed
        # self.firstStation = first
        # self.nextStation = next

    def __repr__(self) -> str:
        return self.toTuple().__str__()

    def getId(self) -> int:
        return self.id

    def getWorksColour(self) -> str:
        if (self.works == 1):
            return "#e39b14"
        else:
            return "#36b325"

    def getStatusColour(self) -> str:
        if (self.status == 0):
            return "#b52424"
        else:
            return "#36b325"

    def toTuple(self) -> tuple:
        """Returns tuple of values in order of columns in database"""
        return (self.id, self.name, self.numOfCameras, self.prevalence, self.works, self.status)