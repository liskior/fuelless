import random

from src.generator import Reasons


class TrafficJam:
    length = 0
    avg_speed = 0
    reason = 0
    start_time = 0
    end_time = 0
    def __init__(self):
        self.length = round(random.uniform(1, 15), 2)
        self.avg_speed = round(random.uniform(2.5, 10), 2)
        self.reason = random.choice(list(Reasons))
        self.start_time = round(random.uniform(1, 15), 2)
    def __str__(self):
        return '[Length: %s]' % (self.length) + \
               '[Average speed: %s]' % (self.avg_speed) +\
               '[Reason: %s]' % (self.reason) + \
               '[Start time: %s]' % (self.start_time)