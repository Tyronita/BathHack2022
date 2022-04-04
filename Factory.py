import csv
from random import shuffle, randint
from re import S
from sre_parse import State
from DatabaseModel import DatabaseConnection
from StationModel import StationModel
from LineModel import LineModel

def main():
    stations = []
    with open('stations.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                for i in range(0, 7, 2):
                    cell = row[i]
                    if cell != "":
                        stations.append(row[i])
                        line_count += 1
            else:
                line_count += 1

    shuffle(stations)

    db: DatabaseConnection = DatabaseConnection()

    network_stations = stations[:16]
    network_lines = ["Benardis Line", "Turing Line", "Fabio Line", "Nickoli Line"]
    line_colours = ["#4287f5", "#3aad2d", "#a62121", "#ab208d"]

    # for stationName in network_stations:
    #     station = generateStation(stationName)
    #     print("Inserting station")
    #     db.insert_station(station)

    # for lineName, lineColour in zip(network_lines, line_colours):
    #     line = generateLine(lineName, lineColour)
    #     print("Inserting line")
    #     db.insert_line(line)


    l = generateLine("aseff", "sf")
    s = generateStation("asdf")
    
    l.id = 1
    s.id = 1
    db.insert_line_station(l, s, 1)
    s.id = 6
    db.insert_line_station(l, s, 2)
    s.id = 10
    db.insert_line_station(l, s, 3)
    s.id = 14
    db.insert_line_station(l, s, 4)

    l.id = 2
    s.id = 2
    db.insert_line_station(l, s, 1)
    s.id = 4
    db.insert_line_station(l, s, 2)
    s.id = 10
    db.insert_line_station(l, s, 3)
    s.id = 11
    db.insert_line_station(l, s, 4)
    s.id = 12
    db.insert_line_station(l, s, 5)

    l.id = 3
    s.id = 3
    db.insert_line_station(l, s, 1)
    s.id = 4
    db.insert_line_station(l, s, 2)
    s.id = 5
    db.insert_line_station(l, s, 3)
    s.id = 6
    db.insert_line_station(l, s, 4)
    s.id = 7
    db.insert_line_station(l, s, 5)
    s.id = 8
    db.insert_line_station(l, s, 6)
    s.id = 9
    db.insert_line_station(l, s, 7)

    l.id = 4
    s.id = 13
    db.insert_line_station(l, s, 1)
    s.id = 14
    db.insert_line_station(l, s, 2)
    s.id = 15
    db.insert_line_station(l, s, 3)
    s.id = 16
    db.insert_line_station(l, s, 4)


def generateStation(stationName):
    numCameras = randint(1, 3)
    prevalence = randint(1, 10)
    value = randint(0, 100)
    if value >= 10:
        works = 0
    else:
        works = 1

    value = randint(0, 100)
    if value >= 10:
        status = 1
    else:
        status = 0

    return StationModel(0, stationName, numCameras, prevalence, works, status)

def generateLine(lineName, lineColour):
    return LineModel(0, lineName, 1, lineColour)

if __name__ == "__main__":
    main()