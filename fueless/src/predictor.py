

# Create first network with Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
import generator

class Predictor:
    def __init__(self):
        # fix random seed for reproducibility
        seed = 7
        numpy.random.seed(seed)

        # load some random simulated dataset with parameters of traffic jams
        # split into input (X) and output (Y) variables
        training_data, validation_data, test_data = generator.generateTrafficJams()
        X = training_data[:, 0:4]
        Y = training_data[:, 4]  # labels

        # create model
        self.model = Sequential()
        self.model.add(Dense(12, input_dim=4, init='uniform', activation='relu'))
        self.model.add(Dense(1, init='uniform', activation='relu'))
        # Compile model
        self.model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])
        # Fit the model
        self.model.fit(X, Y, nb_epoch=1, batch_size=10, verbose=2)
        # calculate predictions
        predictions = self.model.predict(X)
        print(self.model.predict(numpy.random.rand(1, 4)))
        print(self.predict(numpy.random.rand(1, 4)))
        # round predictions
        rounded = [round(x[0]) for x in predictions]
        print(rounded)

    def predict(self, traffic_jam):
        return self.model.predict(traffic_jam)




