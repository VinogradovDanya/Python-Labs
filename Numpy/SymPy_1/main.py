from math import exp


def s(x):
    return 1 / (1 + exp(-x / 10))


def main():
    stud_levels = [int(i) for i in input().split()]
    n = len(stud_levels)
    task_levels = [int(i) for i in input().split()]
    k = len(task_levels)
    q = 0
    for student in stud_levels:
        m = 0
        for task in task_levels:
            m += s(student - task)
        if m >= 0.5 * k:
            q += 1
    print(q)


if __name__ == "__main__":
    main()
