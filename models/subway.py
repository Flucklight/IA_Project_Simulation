class Subway:
    def __init__(self, position):
        self.position = position
        self.back_station = position
        self.line = position.line
        for station in position.stations:
            if station.line.__contains__(self.line):
                self.forward_station = station

    def go_forward(self):
        self.back_station = self.position
        self.position = self.forward_station
        for station in self.forward_station.stations:
            if station != self.back_station and station.line.__contains__(self.line):
                self.forward_station = station
                break
        if self.position == self.forward_station:
            self.forward_station = self.back_station
