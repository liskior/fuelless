import random
import src.generator as gen
import src.traffic_jam as tj

class Jam_Simulator:

    def generate_traffic_jams(self, route_length):
        traffic_jams = []

        for i in range(random.randint(1, 6)):
            jam = tj.TrafficJam

            while True:
                jam.start = random.randint(route_length)

                for j in range(i):
                    if jam.overlaps(traffic_jams[j]):
                        break
                else:
                    traffic_jams.append(jam)
                    break

        # sort the traffic jams
        traffic_jams = sorted(traffic_jams, key=lambda traffic_jam: traffic_jam.start)

        return traffic_jams