from numpy import matrix
from numpy.linalg import matrix_power

N = input()
N = int(N)
arr = []
vec_arr = []

s = input()
s = s.split(' ')
for i in s:
    vec_arr.append(float(i))

for i in range(N):
    arr.append([])
    s = input()
    s = s.split(' ')
    for j in s:
        arr[i].append(float(j))

matr = matrix(arr)

vec = matrix([[i, ] for i in vec_arr])
k = int(input())

ans = (matr**k) * vec
for i in ans:
    print(i.item(0))
