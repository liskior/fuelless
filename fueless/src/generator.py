import random

import numpy as np

from traffic_jam import TrafficJam, Reasons


def get_jam(length = 0, number = 0):
    jam = TrafficJam()
    if not length:
         jam.length = round(random.uniform(1, 15), 2)
    jam.avg_speed = round(random.uniform(2.5, 10), 2)
    jam.reason = random.randint(1, 4)
    jam.start_time = round(random.uniform(1, 15), 2)
    jam.number = number
    jam.end = round(random.uniform(1, 9), 2)
    a = np.array([jam.length, jam.avg_speed, jam.reason, jam.start_time, jam.end]).reshape((1, 5))
    #print(a)
    return a




def generate():
    training_data = get_jam()
    for i in range(40000):
        training_data = np.concatenate([training_data, get_jam()])

    validation_data = get_jam()
    for i in range(20000):
        validation_data = np.concatenate([validation_data, get_jam()])
    test_data = get_jam()
    for i in range(10000):
        test_data = np.concatenate([test_data, get_jam()])

    return training_data, validation_data, test_data