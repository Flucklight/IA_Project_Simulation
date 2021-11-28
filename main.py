import random as rd

from models.stations_network import StationsNetwork
from models.subway import Subway
from models.user import User


def simulation():
    in_network = []
    while len(users_list) > 0 or len(in_network) > 0:
        new_inside_user = rd.randint(0, 2)
        if new_inside_user == 1 and len(users_list) != 0:
            user = users_list.pop()
            user.inside = True
            user.position.users += 1
            user.get_path()
            in_network.append(user)
            print('El usuario {} entro a la red en {} con destino a {}'.format(user.name, user.start.name, user.dest.name))
        for user in in_network:
            if user.inside:
                for subway in subways:
                    if not user.traveling and subway.position == user.position and subway.forward_station == user.forward:
                        user.traveling = True
                        print('El usuario {} subio al metro en la estacion {}'.format(user.name, user.position.name))
                        break
                    elif user.traveling and subway.position == user.position and subway.forward_station != user.forward:
                        user.traveling = False
                        print('El usuario {} bajo del metro en la estacion {}'.format(user.name, user.position.name))
                    subway.go_forward()
                    print('El metro de la linea {} avanzo a la estacion {}'.format(subway.line, subway.position.name))
                user.position.users -= 1
                user.go_forward()
                user.position.users += 1
            else:
                in_network.remove(user)
                print('El usuario {} salio  de la red'.format(user.name, user.position))


if __name__ == '__main__':
    station_network = StationsNetwork()
    subways = []
    for station in station_network.stations:
        if station.name == 'Observatorio' or station.name == 'Cuatro caminos' or station.name == 'Indios Verdes' or station.name == 'Talisman' or station.name == 'Politecnico' or station.name == 'Tezozomoc' or station.name == 'Barranca del Muerto' or station.name == 'Constitucion de 1917' or station.name == 'Puebla' or station.name == 'Agricola Oriental' or station.name == 'Ciudad Azteca' or station.name == 'Tlahuac':
            subways.append(Subway(station))
    users_list = []
    for i in range(1000):
        start = station_network.stations[rd.randint(0, len(station_network.stations) - 1)]
        dest = station_network.stations[rd.randint(0, len(station_network.stations) - 1)]
        if start == dest:
            dest = station_network.stations[rd.randint(0, len(station_network.stations) - 1)]
        users_list.append(User(i, start, dest))
    simulation()
