import numpy
import math


def min_penalty(a, p, q):
    p_matrix = [float('inf')]*(len(a)-1)
    back_track = {}

    for i in range(q-1, p-1, -1):
        for j in range(i+1, q+1):
            num = a[j]-a[i]
            if num <= 200:
                if j == q:
                    val = charge(num)
                    if val < p_matrix[i]:
                        p_matrix[i] = val
                        back_track[i] = i, j
                elif i < j:
                    num = charge(num)
                    num_min = p_matrix[j]
                    val = num + num_min
                    if val < p_matrix[i]:
                        p_matrix[i] = val
                        back_track[i] = i, j

    print(p_matrix)
    tour_path = []
    k = 0
    print(back_track)
    while k < len(p_matrix):
        m, j = back_track[k]
        tour_path.append(j)
        k = j

    return p_matrix[0], tour_path


def charge(n):
    return math.pow(200-n, 2)


if __name__ == "__main__":
    arr = [0, 130, 180, 330, 380]
    prob = min_penalty(arr, 0, len(arr)-1)
    print(prob)

