import random
import generator as gen
import traffic_jam as tj

from generator import generate

from traffic_jam import TrafficJam


class Jam_Simulator:

    def generate_traffic_jams(self, route_length):
        traffic_jams = []

        for i in range(random.randint(1, 6)):
            jam = TrafficJam()
            jam.length = round(random.uniform(1, 15), 2)
            jam.avg_speed = round(random.uniform(2.5, 10), 2)
            jam.reason = random.randint(1, 4)
            jam.start_time = round(random.uniform(1, 15), 2)


            while True:
                jam.start = random.randint(0, route_length)

                for j in range(i):
                    if jam.overlaps(traffic_jams[j]):
                        break
                else:
                    traffic_jams.append(jam)
                    break

        # sort the traffic jams
        traffic_jams = sorted(traffic_jams, key=lambda traffic_jam: traffic_jam.start)
        print(traffic_jams)

        return traffic_jams