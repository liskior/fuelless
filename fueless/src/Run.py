from predictor import Network
from predictor import FullyConnectedLayer
import generator


def main():
    net = Network([FullyConnectedLayer(n_in = 4, n_out = 1)], mini_batch_size=1000)
    training_data, validation_data, test_data= generator.generate()
    net.SGD(training_data= training_data, epochs=40, mini_batch_size=1000, eta=0.005, validation_data= validation_data, test_data=test_data)
    print ("start that, bitches")



if __name__ == "__main__":
    main()