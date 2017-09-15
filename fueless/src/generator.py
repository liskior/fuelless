from enum import Enum

from src.traffic_jam import TrafficJam


class Reasons(Enum):
    accident = 1
    road_works = 2
    unknown = 3

def get_jam() :
    jam = TrafficJam()
    a = []
    a.append(jam.length)
    a.append(jam.avg_speed)
    a.append(jam.reason)
    a.append(jam.start_time)
    return a
print(get_jam())