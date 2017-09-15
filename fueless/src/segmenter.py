import src.segment as seg

SPEED = 120

class Segmenter:

    def get_segmented_route(self, route, traffic_jams):
        segments = []
        current_pos = 0

        for jam in traffic_jams:
            start = jam.start
            if (start != current_pos):
                segments.append(seg.Segment(current_pos, start - current_pos, SPEED))
            segments.append(seg.Segment(start, jam.length, jam.avg_speed, jam))
            current_pos = jam.start + jam.length

        if current_pos < route.length:
            segments.append(seg.Segment(current_pos, route.length - current_pos, SPEED))

        return segments