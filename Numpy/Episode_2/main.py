import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 4):
    data = np.genfromtxt('signal0' + str(i) + '.dat')
    data1 = np.convolve(data, np.ones((10,)) / 10, mode='valid')

    plt.subplot(1, 2, 1)
    plt.grid()
    plt.plot(data)
    plt.title('Сырой сигнал номер ' + str(i))
    plt.subplot(1, 2, 2)
    plt.grid()
    plt.plot(data1)
    plt.title('Обработанный сигнал')
    plt.savefig('signal0' + str(i) + '.png')
    plt.show()
