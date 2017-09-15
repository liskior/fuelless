SEGMENT_SIZE = 0
AVG_SPEED = 120

class Segment:
    def __init__(self, start, jam_info=None):
        self.start = start
        self.length = SEGMENT_SIZE
        self.jam_info = jam_info
        self.avg_speed = AVG_SPEED