import matplotlib.pyplot as plt

class Plotter:
    def __init__(self):
        plt.xlabel('km')
        plt.ylabel('Geschwindigkeit')

    def add_plots(self, x, y, x2, y2):
        plt.plot(x, y, 'r', x2, y2, 'b')

    def draw(self):
        plt.show()