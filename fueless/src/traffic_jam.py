from enum import Enum

class Reasons(Enum):
    accident = 1
    road_works = 2
    unknown = 3


class TrafficJam:
    start = 0
    length = 0
    avg_speed = 0
    reason = 0
    start_time = 0
    number = 0
    end = 0
    def __init__(self, length = 0, number = 0):
        self.length = length

    def __str__(self):
        return '[Length: %s]' % (self.length) + \
               '[Average speed: %s]' % (self.avg_speed) +\
               '[Reason: %s]' % (self.reason) + \
               '[Start time: %s]' % (self.start_time)

    def overlaps(self, other):
        return (self.start > other.start and self.start < other.start + other.length) \
               or (other.start > self.start and other.start < self.start + self.length)