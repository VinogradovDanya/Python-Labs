import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use('dark_background')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


# create a mussive fo lines - put in data(list lines)
data = open('frames.dat', 'r')
print(data)
# create a new lwo list
xs = []
ys = []

for i in data:
    if len(i.split()) == 2:
        plt.axis()
    else:
        xs = [int(x) for x in i.split()]
        ys = [int(y) for y in (i+1).split()]

    ax1.clear()
    ax1.plot(xs, ys)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Обновляемые графики')

animation = ax1.animate()

# Сохраняем анимацию как gif файл
animation.save('animation.gif', writer ='imagemagick')
plt.show()


