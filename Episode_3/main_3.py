import matplotlib.pyplot as plt
from collections import defaultdict

dct1 = defaultdict(list)
dct2 = defaultdict(list)

with open("students.csv") as file:
    line = file.readlines()
    for i in line:
        x = int(i.split(';')[2])
        dct1[i.split(';')[0]].append(x)
        dct2[i.split(';')[1]].append(x)

fig, ax1 = plt.subplots(2, 1, figsize=[12, 12])
w = 0.6

dct1_new = defaultdict(list)
dct2_new = defaultdict(list)
listic = []

for key in dct1:
    for i in range(11):
        dct1[key].count(i)
        dct1_new[key].append([i, dct1[key].count(i)])

for key in dct2:
    for i in range(11):
        dct2[key].count(i)
        dct2_new[key].append([i, dct2[key].count(i)])

print(dct1_new)
print(dct2_new)


for i in range(1, 11):
    rez1 = [dct1_new[key][i][1] for key in dct1_new]
    print(rez1)
    rez2 = [dct2_new[key][i][1] for key in dct2_new]
    print(rez2)
    ax1[0].bar(list(dct1_new.keys()), rez1, w, bottom=rez1, label='%d' % i)
    ax1[1].bar(list(dct2_new.keys()), rez2, w, bottom=rez2, label='%d' % i)


ax1[0].set_title('Marks per prep')
plt.subplots_adjust(wspace=0.5, hspace=0.4)
ax1[1].set_title('Marks per group')
ax1[0].legend(loc='upper right', fontsize=10)
ax1[1].legend(loc='upper right', fontsize=10)
plt.show()
