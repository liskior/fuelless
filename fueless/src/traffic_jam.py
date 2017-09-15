from enum import Enum

class Reasons(Enum):
    accident = 1
    road_works = 2
    unknown = 3


class TrafficJam:
    length = 0
    avg_speed = 0
    reason = 0
    start_time = 0
    def __str__(self):
        return '[Length: %s]' % (self.length) + \
               '[Average speed: %s]' % (self.avg_speed) +\
               '[Reason: %s]' % (self.reason) + \
               '[Start time: %s]' % (self.start_time)