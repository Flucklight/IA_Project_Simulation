from models.station import Station


class StationsNetwork:
    def __init__(self):
        self.stations = []
        with open('assetes/matriz_adyacencia.csv', 'r') as f:
            for name in f.readline()[:-1].split(','):
                data_format = name.split(':')
                self.stations.append(Station(data_format[1], data_format[0]))
            i = 0
            for line in f:
                j = 0
                for data in line[:-1].split(','):
                    if data != '0':
                        self.stations[i].stations.append(self.stations[j])
                    j += 1
                i += 1
        f.close()
