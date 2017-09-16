import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from predictor import Predictor
import numpy


def main():
    predictor = Predictor()


    #for testing
    print(predictor.predict(traffic_jam=numpy.random.rand(1,4)))


if __name__ == "__main__":
    main()