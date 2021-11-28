from models.individual import Individual


def get_grade(individual):
    return individual.grade


class User:
    def __init__(self, name, start, dest):
        self.name = name
        self.path = []
        self.population = []
        self.position = start
        self.start = start
        self.dest = dest
        self.forward = None
        self.inside = False
        self.traveling = False

    def get_path(self):
        self.search(10, 10)
        self.path = self.population[0].gen[1:]
        self.forward = self.path.pop(0)

    def go_forward(self):
        if self.traveling:
            if self.position != self.dest:
                self.position = self.forward
                if len(self.path) != 0:
                    self.forward = self.path.pop(0)
            else:
                self.inside = False

    def gen_population(self, population_length):
        while len(self.population) < population_length:
            self.population.append(Individual(self.start, self.dest, 164))

    def population_average(self):
        average = 0
        for ind in self.population:
            average += ind.grade
        return average / len(self.population)

    def selection(self):
        self.population.sort(key=get_grade)

    def cross_over(self):
        for i in range(int(len(self.population) / 2)):
            self.population.pop()
            self.population.append(self.population[i].clone(self.dest))

    def search(self, population_length, generations_average):
        self.gen_population(population_length)
        gen_memory = []
        global_average = 0
        while True:
            gen_memory.insert(0, self.population_average())
            if len(gen_memory) > generations_average:
                gen_memory.pop()
                memory_average = global_average
                global_average = 0
                for mem in gen_memory:
                    global_average += mem
                global_average = global_average / len(gen_memory)
                if memory_average == global_average:
                    break
            self.selection()
            self.cross_over()
