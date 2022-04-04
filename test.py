from DatabaseModel import DatabaseConnection
from NetworkModel import NetworkModel

class Network:
    # id of each entrys
    def __init__(self):
        db = DatabaseConnection()
        network: NetworkModel = db.get_network()
        lines = network.getLines()
        print("edwada")
        lines[0].getStations()
    
def main():
    db = DatabaseConnection()
    network: NetworkModel = db.get_network()
    lines = network.getLines()
    lines[0].getStations()
    print(lines[0].getStations())
    print(lines[0])

if __name__ == "__main__":
    main()
