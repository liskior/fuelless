class Segment:
    def __init__(self, start, length, avg_speed, jam_info=None):
        self.start = start
        self.length = length
        self.jam_info = jam_info
        self.avg_speed = avg_speed