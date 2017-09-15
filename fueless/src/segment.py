AVG_SPEED = 120

class Segment:
    def __init__(self, start, length, jam_info=None):
        self.start = start
        self.length = length
        self.jam_info = jam_info
        self.avg_speed = AVG_SPEED