
import math


def penalty(a, p, q):

    if p > q:
        return 0

    elif p == q:
        return charge(a[p])

    else:
        fees = float('inf')
        for j in range(p, q+1):
            num = sum(a[p:j+1])

            if num <= 200:
                fees = min(fees, penalty(a, j+1, q) + charge(num))
        return fees


def charge(n):
    return math.pow(200-n, 2)


if __name__ == "__main__":
    arr = [130, 70, 150, 30]
    winner = penalty(arr, 0, len(arr)-1)
    print(winner)

