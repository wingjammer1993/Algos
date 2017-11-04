
import math
import numpy


class SolPenalty:

    def __init__(self, arr_hotel, p, q):
        x = len(arr_hotel)
        self.cost = numpy.empty((x, x))
        self.path = numpy.empty((x, x))
        self.cost[:] = numpy.NAN
        self.path[:] = numpy.float('-inf')
        self.fees = self.penalty(arr_hotel, p, q)
        self.hotels = self.reconstruct_solution(self.path)

    def penalty(self, a, p, q):

        if p > q:
            return 1

        elif p == q:

            self.cost[p][q] = charge(a[p])
            self.path[p][q] = charge(a[p])

        else:
            fees = float('-inf')
            for j in range(p, q+1):
                if j < q and self.cost[j+1][q] >= 0:
                    fees = max(fees, self.cost[j+1][q]*charge(a[p:j+1]))
                else:
                    fees = max(fees, self.penalty(arr, j+1, q)*charge(a[p:j+1]))
                self.path[p][j] = fees
            self.cost[p][q] = fees
        return self.cost[p][q]

    def reconstruct_solution(self, path):
        tour_path = []
        k = 0
        i = 0
        while k < len(path):
            j = numpy.argmax(path[k])
            tour_path.append((i, j))
            i = j+1
            k = j+1
        return tour_path


def charge(string):
    d = {'p': 0.9, 'pa': 0.8, 'pan': 0.2, 'pand': 0.01, 'a': 0.5, 'an': 0.9, 'and': 0.7, 'n': 0.2,
                           'nd': 0.6, 'd': 0.9}
    val = 1
    str_n = string
    if isinstance(string, list):
        str_n = ''
        for elem in string:
            str_n = str(str_n) + str(elem)
    if str_n in d:
        val = d[str_n]
    return val


if __name__ == "__main__":
    arr = 'pand'

    winner = SolPenalty(list(arr), 0, len(arr)-1)
    answer = winner.fees
    costy = winner.cost
    hotels = winner.path
    tour = winner.hotels
    print(hotels)
    print(costy)
    print(answer)
    print(tour)

