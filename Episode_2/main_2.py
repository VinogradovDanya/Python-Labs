import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.style.use('dark_background')
fig, ax1 = plt.subplots(3, 2, figsize=[12, 12])

# create a new lwo list
xs = []
ys = []
n = 0
m = 0

with open("frames.dat") as file:
    while True:
        line1 = file.readline()
        line2 = file.readline()
        if not line2:
            break
        x = [float(i) for i in line1.split()]
        y = [float(i) for i in line2.split()]
        ax1[n, m].plot(x, y)
        ax1[n, m].set_title('Frame %d' % (1 + n + 3 * m))
        ax1[n, m].set_xlim([0, 16])
        ax1[n, m].set_ylim([-12, 12])
        ax1[n, m].grid()
        ax1[n, m].xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax1[n, m].xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
        ax1[n, m].yaxis.set_major_locator(ticker.MultipleLocator(2))
        ax1[n, m].yaxis.set_minor_locator(ticker.MultipleLocator(1))
        for label in (ax1[n, m].get_xticklabels() + ax1[n, m].get_yticklabels()):
            label.set_fontsize(8)
        if n == 2:
            n = 0
            m += 1
        else:
            n += 1

plt.subplots_adjust(wspace=0.5, hspace=0.4)
plt.savefig("res.png")
plt.close(fig)
plt.show()
