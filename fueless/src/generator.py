import random

from src.traffic_jam import TrafficJam, Reasons
import numpy as np


def get_jam():
    jam = TrafficJam()
    jam.length = round(random.uniform(1, 15), 2)
    jam.avg_speed = round(random.uniform(2.5, 10), 2)
    jam.reason = random.choice(list(Reasons))
    jam.start_time = round(random.uniform(1, 15), 2)
    a = np.array([jam.length, jam.avg_speed, jam.reason, jam.start_time])
    return (a, round(random.uniform(1, 8), 2))

print(get_jam())


def generate():
    training_data = []
    for i in range(40000):
        training_data.append(get_jam())
    validation_data = []
    for i in range(20000):
        validation_data.append(get_jam())
    test_data = []
    for i in range(10000):
        test_data.append(get_jam())
    return training_data, validation_data, test_data
