import random
import src.generator as gen

class Jam_Simulator:

    def generate_traffic_jams(self, route_length):
        traffic_jams = []

        for i in range(random.randint(1, 11)):
            traffic_jams.append(gen.get_jam())



        return traffic_jams