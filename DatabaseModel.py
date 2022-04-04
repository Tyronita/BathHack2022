import sqlite3
from typing import List
from constants import *
from LineModel import LineModel
from StationModel import StationModel
from NetworkModel import NetworkModel

class DatabaseConnection:
    def __init__(self) -> None:
        try:
            self.conn = sqlite3.connect(DATABASE_NAME)
            self.cur = self.conn.cursor()
        except sqlite3.Error as error:
            print("Unable to open database")
            return
        # self.createTables()
        

    def createTables(self) -> None:
        self.cur.execute("CREATE TABLE "+STATIONS_TABLE+" ("
                "station_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "station_name TEXT NOT NULL,"
                "station_cameras INTEGER NOT NULL,"
                "station_prevalence INTEGER,"
                "station_works INTEGER NOT NULL,"
                "station_status INTEGER NOT NULL"
                # "station_first INTEGER,"
                # "station_next INTEGER,"
                # "FOREIGN KEY (station_next) REFERENCES "+STATIONS_TABLE+"(station_id)"
            ")")

        self.cur.execute("CREATE TABLE "+LINES_TABLE+" ("
                "line_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "line_name TEXT,"
                "line_status INTEGER,"
                "line_colour TEXT"
            ")")

        self.cur.execute("CREATE TABLE "+LINE_STATIONS_TABLE+" ("
                "line_id INTEGER,"
                "station_id INTEGER,"
                "station_num INTEGER,"
                "FOREIGN KEY(line_id) REFERENCES "+LINES_TABLE+"(line_id),"
                "FOREIGN KEY(station_id) REFERENCES "+STATIONS_TABLE+"(station_id),"
                "PRIMARY KEY (line_id, station_id)"
            ")")

    def get_lines(self) -> List:
        self.cur.execute(
            "SELECT * FROM "+LINES_TABLE
        )
        rows = self.cur.fetchall()
        lines = []
        for row in rows:
            lines.append(LineModel(*row))
        return lines

    def get_stations_on_line(self, lineModel: LineModel) -> List:
        self.cur.execute(
            "SELECT  "+STATIONS_TABLE+".station_id, station_name, station_cameras, station_prevalence, station_works, station_status "
            "FROM "+LINE_STATIONS_TABLE+" "
            "INNER JOIN "+STATIONS_TABLE+" ON "+LINE_STATIONS_TABLE+".station_id = "+STATIONS_TABLE+".station_id "
            "WHERE line_id = ? "
            "ORDER BY "+LINE_STATIONS_TABLE+".station_num",
            (lineModel.getId(), )
        )
        rows = self.cur.fetchall()
        stations = []
        for row in rows:
            stations.append(StationModel(*row))
        return stations

    def get_network(self) -> NetworkModel:
        lines = self.get_lines()
        for line in lines:
            line.stations = self.get_stations_on_line(line)
        return NetworkModel(lines)

    def insert_station(self, stationModel: StationModel):
        self.cur.execute(
            "INSERT INTO "+STATIONS_TABLE+"(station_name, station_cameras, station_prevalence, station_works, station_status) VALUES (?,?,?,?,?)", stationModel.toTuple()[1:]
            )
        self.conn.commit()

    def insert_line(self, lineModel: LineModel):
        self.cur.execute("INSERT INTO "+LINES_TABLE+"(line_name, line_status, line_colour) VALUES (?,?,?)", lineModel.toTuple()[1:])
        self.conn.commit()

    def insert_line_station(self, lineModel: LineModel, stationModel: StationModel, lineNum: int):
        self.cur.execute("INSERT INTO "+LINE_STATIONS_TABLE+" VALUES (?,?,?)", (lineModel.getId(), stationModel.getId(), lineNum))
        self.conn.commit()

    def update_station(self, stationModel: StationModel):
        self.cur.execute(
            "UPDATE "+STATIONS_TABLE+" SET "
            "station_name=?,"
            "station_cameras=?,"
            "station_prevalence=?,"
            "station_works=?,"
            "station_status=? "
            # "station_first=?,"
            # "station_next=? "
            "WHERE station_id = ?",
            (stationModel.toTuple()[1:] + (stationModel.getId(), ))
        )
        self.conn.commit()

    def update_line(self, lineModel: LineModel):
        self.cur.execute(
            "UPDATE "+STATIONS_TABLE+" SET "
            "line_name=?,"
            "line_status=?,"
            "line_colour=? "
            "WHERE line_id = ?",
            (lineModel.toTuple()[1:] + (lineModel.getId(), ))
        )
        self.conn.commit()

    def delete_station(self, stationModel: StationModel):
        self.cur.execute(
            "DELETE FROM "+STATIONS_TABLE+" WHERE station_id = ?",
            (stationModel.getId(), )
        )
        self.conn.commit()

    def delete_line(self, lineModel: LineModel):
        self.cur.execute(
            "DELETE FROM "+LINES_TABLE+" WHERE line_id = ?",
            (lineModel.getId(), )
        )
        self.conn.commit()

    def delete_line_station(self, lineModel: LineModel, stationModel: StationModel):
        self.cur.execute(
            "DELETE FROM "+LINE_STATIONS_TABLE+" WHERE station_id = ? AND line_id = ?",
            (stationModel.getId(), lineModel.getId())
        )
        self.conn.commit()



def main():
    db = DatabaseConnection()
    network: NetworkModel = db.get_network()
    lines = network.getLines()
    for line in lines:
        print(line.getStations())


if __name__ == "__main__":
    main()