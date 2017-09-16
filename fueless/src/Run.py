import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from predictor import Predictor
import numpy

from optimizer import optimize


def main():
    predictor = Predictor()
    optimize()


if __name__ == "__main__":
    main()