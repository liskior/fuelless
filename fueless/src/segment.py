AVG_SPEED = 130

class Segment:
    def __init__(self, start, length, number, jam_info=None):
        self.start = start
        self.length = length
        self.jam_info = jam_info
        self.avg_speed = AVG_SPEED
        self.number = number
    def __str__(self):
        return '[Length: %s]' % (self.length) + \
               '[Average speed: %s]' % (self.avg_speed) + \
               '[Start: %s]' % (self.start) + \
               '[Number: %s]' % (self.number)