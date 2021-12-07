import numpy as np


def main():
    file_name = input()
    with open(file_name, "r") as file:
        n = int(file.readline())
        k = []
        for i in range(2 * n):
            k.append([float(i) for i in file.readline().split()])
        k = np.array(k)
        f = np.array([float(i) for i in file.readline().split()])
    a = np.transpose(k).dot(f)
    a = a.tolist()[::2]
    ans = min(a)
    print(-ans if ans < 0 else 0)


if __name__ == "__main__":
    main()
