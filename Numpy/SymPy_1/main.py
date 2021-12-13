import numpy as np
import numpy.linalg as lin



failic = open(input(), "r")
n = int(failic.readline())
k = []

for i in range(2 * n):
    k.append([float(i) for i in failic.readline().split()])

k_1 = np.array(k)
f_2 = np.array([float(i) for i in failic.readline().split()])
tochno = np.dot(lin.inv(k_1), f_2)
toch = tochno.tolist()[::2]
ans = min(toch)
print(-ans if ans < 0 else 0)
