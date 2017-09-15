import random

from src.traffic_jam import TrafficJam
import numpy as np


def get_jam():
    jam = TrafficJam()
    a = np.array()
    b = np.array()
    a.append(jam.length)
    a.append(jam.avg_speed)
    a.append(jam.reason)
    a.append(jam.start_time)
    b.append(a)
    b.append(round(random.uniform(1, 8), 2))
    return b

print(get_jam())

def generate():
<<<<<<< HEAD
    c = np.array()
    for i in range(40000):
        c.append(get_jam())
    d = np.array()
    for i in range(20000):
        c.append(get_jam())
    e = np.array()
=======
    training_data = []
    for i in range(40000):
        training_data.append(get_jam())
    validation_data = []
    for i in range(20000):
        validation_data.append(get_jam())
    test_data = []
>>>>>>> 74bf7d399231d4028357c7f6a9e9e5700af9e18a
    for i in range(10000):
        test_data.append(get_jam())
    return training_data, validation_data, test_data