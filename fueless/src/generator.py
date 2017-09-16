import random

from src.traffic_jam import TrafficJam, Reasons
import numpy as np


#generate random trainings, validation and test data
def generateTrafficJams():
    return np.random.rand(10000, 5), np.random.rand(10000, 5), np.random.rand(10000, 5)
