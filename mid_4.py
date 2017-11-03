
import math
import numpy


class SolPenalty:

    def __init__(self, arr_hotel, p, q):
        x = len(arr_hotel)
        self.cost = numpy.empty((x, x))
        self.path = numpy.empty((x, x))
        self.cost[:] = numpy.NAN
        self.path[:] = numpy.float('inf')
        self.fees = self.penalty(arr_hotel, p, q)
        self.hotels = self.reconstruct_solution(self.path)

    def penalty(self, a, p, q):

        if p > q:
            return 0

        elif p == q:
            self.cost[p][q] = self.charge(a[p])
            self.path[p][q] = self.charge(a[p])

        else:
            fees = float('inf')
            for j in range(p, q+1):
                num = sum(a[p:j+1])
                if num <= 200:
                    if j < q and self.cost[j+1][q] >= 0:
                        fees = min(fees, self.cost[j+1][q] + self.charge(num))
                    else:
                        fees = min(fees, self.penalty(arr, j+1, q) + self.charge(num))
                    self.path[p][j] = fees
            self.cost[p][q] = fees
        return self.cost[p][q]


    def charge(self, n):
        return math.pow(200-n, 2)

    def reconstruct_solution(self, path):
        tour_path = []
        k = 0
        i = 0
        while k < len(path):
            j = numpy.argmin(path[k])
            tour_path.append((i, j))
            i = j+1
            k = j+1
        return tour_path


if __name__ == "__main__":
    arr = [130, 50, 150, 50, 120]
    winner = SolPenalty(arr, 0, len(arr)-1)
    answer = winner.fees
    costy = winner.cost
    hotels = winner.path
    tour = winner.hotels
    print(hotels)
    print(costy)
    print(answer)
    print(tour)

