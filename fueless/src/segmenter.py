import src.segment as seg

SPEED = 120

class Segmenter:

    def get_segmented_route(self, route, traffic_jams):
        segments = []
        passed_jams = 0

        for i in range(route.length):
            if i < traffic_jams[passed_jams].start or len(traffic_jams) == passed_jams:
                segments.append(seg.Segment(i))
            else:
                for j in range(len(traffic_jams) - passed_jams):
                    if traffic_jams[j].start + traffic_jams[j].length >= i:
                        if len(segments) == i:
                            segments.append(seg.Segment(i, traffic_jams[j]))
                        else:
                            segments[i].jam_info.append(traffic_jams[j])
                    else:
                        passed_jams += 1
        
        return segments