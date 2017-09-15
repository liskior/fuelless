import random

from src.traffic_jam import TrafficJam


def get_jam() :
    jam = TrafficJam()
    a = []
    a.append(jam.length)
    a.append(jam.avg_speed)
    a.append(jam.reason)
    a.append(jam.start_time)
    a.append(round(random.uniform(1, 8), 2))
    return a
print(get_jam())