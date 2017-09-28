

class NumWays:
    def __init__(self):
        self.ways = 0

    def n_cents_ways(self, n, caller=100):

        if n == 0:
            print("returning")
            self.ways = self.ways+1

        if n > 0:
            # divide the number in 25s
            if int(n / 25) and 25 <= caller:
                print("25")
                self.n_cents_ways(n - 25, 25)

            # divide the number in 10s
            if int(n / 10) and 10 <= caller:
                print("10")
                self.n_cents_ways(n - 10, 10)

            # divide the number in 5s
            if int(n / 5) and 5 <= caller:
                print("5")
                self.n_cents_ways(n - 5, 5)

            # divide the number in 1s
            if int(n / 1) and 1 <= caller:
                print("1")
                self.n_cents_ways(n - 1, 1)

        return self.ways


if __name__ == "__main__":

    num_ways = NumWays()
    number_ways = num_ways.n_cents_ways(16)
    print(number_ways)

