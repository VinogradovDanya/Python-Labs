import matplotlib.pyplot as plt
import collections

dct1 = collections.defaultdict(list)
dct2 = collections.defaultdict(list)

with open("students.csv") as file:
    line = file.readlines()
    for i in line:
        x = int(i.split(';')[2])
        dct1[i.split(';')[0]].append(int(x))
        dct2[i.split(';')[1]].append(int(x))

fig, ax1 = plt.subplots(2, 1, figsize=[12, 12])
w = 0.6

for key in dct1:
    a = [0] * 11
    for i in range(11):
        a[i] = dct1[key].count(i)
    dct1[key] = a

for key in dct2:
    a = [0] * 11
    for i in range(11):
        a[i] = dct2[key].count(i)
    dct2[key] = a


for i in range(1, 11):
    rez1 = [dct1[key][i] for key in dct1]
    oldst = [sum(dct1[key][j] for j in range(i)) for key in dct1]
    rez2 = [dct2[key][i] for key in dct2]
    olddt = [sum(dct2[key][j] for j in range(i)) for key in dct2]
    ax1[0].bar(list(dct1.keys()), rez1, w, bottom=oldst, label='%d' % i)
    ax1[1].bar(list(dct2.keys()), rez2, w, bottom=olddt, label='%d' % i)


ax1[0].set_title('Marks per prep')
plt.subplots_adjust(wspace=0.5, hspace=0.4)
ax1[1].set_title('Marks per group')
ax1[0].legend(loc='upper right', fontsize=10)
ax1[1].legend(loc='upper right', fontsize=10)
plt.savefig("res.png")
plt.show()
