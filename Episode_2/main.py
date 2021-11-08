import matplotlib.pyplot as plt


plt.style.use('dark_background')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


data = open('frames.dat', 'r').read()

# create a new lwo list
xs = []
ys = []
a = len(data)
k = 0

for i in data:
    if k % 2 != 0:
        xs = [int(x) for x in i.split()]
        k += 1
    else:
        ys = [int(x) for x in i.split()]
        k += 1

ax1.clear()
ax1.plot(xs, ys)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Обновляемые графики')
plt.show()
