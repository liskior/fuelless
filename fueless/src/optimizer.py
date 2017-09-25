from generator import get_jam
from predictor import Predictor
from segmenter import Segmenter
import numpy as np

from jam_simulator import Jam_Simulator

def optimize(avg_speed=130, length = 1055):
    jams = Jam_Simulator()
    segmenter = Segmenter()
    segmenter = segmenter.get_segmented_route(length, jams.generate_traffic_jams(route_length=length))
    predictor = Predictor()

    print(segmenter)
    jams = []

    for segment in segmenter:
        if not segment.jam_info == None:
            jam = segment.jam_info
            jam.number = segment.number
            jams.append(jam)
            jam.end = round(predictor.predict(np.array([jam.length, jam.avg_speed, jam.reason,
                                                        jam.start_time]).reshape((1, 4)))[0][0], 2)
            print(segment.number)
            print("******")

    for jam in reversed(jams):

        strecke = segmenter[jam.number].start

        avg_speed = min(avg_speed, round(strecke / jam.end, 2))

        if avg_speed < 40:
            stri = str("roads are bad. stay at home.")
            f = open("../templates/tmp.txt", "w")
            f.write(stri)
            f.close()
            return "roads are bad. stay at home."

        for i in range(jam.number):
            (segmenter[i]).avg_speed = avg_speed


    time = 0
    benzin = 0
    strom = 0


    stri = str()
    stri += "length, speed\n"

    for segment in segmenter:
        print(segment.number)
        print(round(segment.length, 2))
        print()

        stri += "[" + str(round(segment.length, 2)) + ", " + str(round(segment.avg_speed, 2)) + "]\n"
        time += segment.length / segment.avg_speed
        benzin += (3.4 + 0.00966667 * segment.avg_speed - 0.00024 * (segment.avg_speed**2) \
                  + 2.53333*(10**(-6))*(segment.avg_speed**3)) * (segment.length * 0.01)
        strom += (-1.1 + 0.06*segment.avg_speed - 0.00025*(segment.avg_speed**2)) * (segment.length * 0.01)


    print("time:")
    print(round(time, 2))
    print("benzin")
    print(round(benzin, 2))
    print("strom")
    print(round(strom, 2))
    stri += "Time: " + str(round(time, 2)) + "\n"
    stri += "Benzin: " + str(round(benzin, 2)) + "\n"
    stri += "Strom: " + str(round(strom, 2)) + "\n"
    f = open("../templates/tmp.txt", "w")
    f.write(stri)
    f.close()

