
import matplotlib.pyplot as plt
f = open('005.dat', 'r')

a = 0
k = 0
x = []
y = []

while True:
    # считываем строку
    line = f.readline()
    print(line.split())
    if k == 0:
        a += int(line)
    else:
        if k == a+1:
            break
        else:
            r = line.split()
            x.append(float(r[0]))
            y.append(float(r[1]))
    # прерываем цикл, если строка пустая
    if not line:
        break
    k+=1


f.close()
plt.plot(x, y, 'ro')
plt.grid()
plt.legend()
plt.show()


