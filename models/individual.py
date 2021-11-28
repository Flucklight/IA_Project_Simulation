import random as rd


class Individual:
    def __init__(self, start, end, stations, clone=False, gen=None):
        if gen is None:
            self.gen = []
        else:
            self.gen = gen
        self.grade = 0
        if not clone:
            self.gen_code(start, end, stations)
        else:
            self.mute(end, stations)

    def gen_code(self, head, tail, stations):
        pointer = head
        backtrack = pointer
        code = []
        cycle = False
        while len(code) < stations and not cycle:
            code.append(pointer)
            if pointer == tail:
                break
            change = rd.randint(0, len(pointer.stations) - 1)
            next_station = pointer.stations[change]
            if next_station == backtrack and len(pointer.stations) != 1:
                if change == len(pointer.stations) - 1:
                    change -= 1
                else:
                    change += 1
                next_station = pointer.stations[change]
            backtrack = pointer
            pointer = next_station
            cycle = code.__contains__(pointer)
        self.gen.extend(code)
        self.evaluation(cycle)

    def evaluation(self, cycle):
        mem_line = self.gen[0].line
        population = 0
        transshipment = 0
        if cycle:
            exponent = 2
        else:
            exponent = 1
        for station in self.gen:
            population += station.users
            if not station.line.__contains__(mem_line):
                transshipment += 1
                mem_line = station.line
        self.grade = pow(len(self.gen), exponent) + transshipment + population

    def clone(self, end):
        return Individual(start=self.gen[0], end=end, stations=164, clone=True, gen=self.gen.copy())

    def mute(self, end, stations):
        change = []
        for allele in self.gen:
            if len(allele.line) > 3:
                change.append(allele)
        if len(change) != 0:
            mute_probability = rd.randint(0, len(change) - 1)
            change = change[mute_probability]
        else:
            mute_probability = rd.randint(0, len(self.gen) - 1)
            change = self.gen[mute_probability]
        for i in range(len(self.gen)):
            if self.gen[-1] != change:
                self.gen.pop()
            else:
                self.gen.pop()
                break
        self.gen_code(change, end, stations)
