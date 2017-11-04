import numpy
import math


def min_penalty(a, p, q):
    p_matrix = numpy.empty((len(a), len(a)))
    p_matrix[:] = numpy.float('inf')

    for i in range(q, p-1, -1):
        for j in range(i, q+1):
            num = sum(a[i:j + 1])
            if num <= 200:
                if j == q:
                    p_matrix[i][j] = charge(num)
                elif i <= j:
                    num = charge(num)
                    num_min = numpy.min(p_matrix[j+1])
                    p_matrix[i][j] = num + num_min

    tour_path = []
    k = 0
    i = 0
    while k < len(p_matrix):
        j = numpy.argmin(p_matrix[k])
        tour_path.append((i, j))
        i = j+1
        k = j+1

    return numpy.min(p_matrix[0]), tour_path


def charge(n):
    return math.pow(200-n, 2)


if __name__ == "__main__":
    arr = [130, 50, 150, 50, 120]
    prob = min_penalty(arr, 0, len(arr)-1)
    print(prob)