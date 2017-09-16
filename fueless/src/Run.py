
from predictor import Predictor
import numpy


def main():
    predictor = Predictor()


    #for testing
    predictor.predict(numpy.random.rand(1,4))



if __name__ == "__main__":
    main()