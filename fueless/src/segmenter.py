import segment as seg

SPEED = 130

class Segmenter:

    def get_segmented_route(self, route, traffic_jams):
        segments = []
        current_pos = 0

        number = 0
        for jam in traffic_jams:
            if jam.start > current_pos:
                segments.append(seg.Segment(current_pos, jam.start - current_pos, number))
                number += 1
            segments.append(seg.Segment(jam.start, jam.length, number, jam))
            number += 1
            current_pos = jam.start + jam.length

        if current_pos < route:
            segments.append(seg.Segment(current_pos, route - current_pos, number))

        
        return segments