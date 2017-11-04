import numpy
import math


def min_penalty(a, p, q):
    p_matrix = [float('inf')]*len(a)
    back_track = {}

    for i in range(q, p-1, -1):
        for j in range(i, q+1):
            num = sum(a[i:j + 1])
            if num <= 200:
                if j == q:
                    val = charge(num)
                    if val < p_matrix[i]:
                        p_matrix[i] = val
                        back_track[i] = i, j
                elif i <= j:
                    num = charge(num)
                    num_min = p_matrix[j+1]
                    val = num + num_min
                    if val < p_matrix[i]:
                        p_matrix[i] = val
                        back_track[i] = i, j

    tour_path = []
    k = 0
    print(back_track)
    while k < len(p_matrix):
        m, j = back_track[k]
        tour_path.append((m, j))
        k = j+1

    return p_matrix[0], tour_path


def charge(n):
    return math.pow(200-n, 2)


if __name__ == "__main__":
    arr = [130, 50, 150, 50, 50, 50, 50, 150]
    prob = min_penalty(arr, 0, len(arr)-1)
    print(prob)

