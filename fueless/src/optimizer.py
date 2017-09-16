from generator import get_jam
from predictor import Predictor
from segmenter import Segmenter
import numpy as np

from jam_simulator import Jam_Simulator


def optimize():
    avg_speed = 130
    jams = Jam_Simulator()
    segmenter = Segmenter()
    segmenter = segmenter.get_segmented_route(1055, jams.generate_traffic_jams(route_length=1055))
    predictor = Predictor()

    print(segmenter)
    jams = []

    for segment in segmenter:
        if not segment.jam_info == None:
            jam = segment.jam_info
            jam.number = segment.number
            jams.append(jam)
            jam.end = predictor.predict(np.array([jam.length, jam.avg_speed, jam.reason, jam.start_time]).reshape((1, 4)))[0][0]
            print(jam.end)
            print(segment.number)
            print("******")

    for jam in reversed(jams):
        strecke = 0
        for i in range(jam.number):
            if not segmenter[i].jam_info:
                strecke += segmenter[i].length
        for i in range(jam.number, len(segmenter)):
            segmenter[i].avg_speed = avg_speed
        avg_speed = min(130, strecke / jam.end)



    for segment in segmenter:
        print(segment.length)
        print(segment.avg_speed)
        print(segment.__str__())
        print()


optimize()