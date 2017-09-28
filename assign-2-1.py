import sys
import baseconvert

# function karatsuba_multiplication implements karatsuba's multiplication algorithm
# param a = Number 1 in base converted to 10
# param b = Number 2 in base converted to 10
# param c = base


def karatsuba_multiplication(a, b, r):

    # If lengths of numbers are 1, directly multiply
    # This is the exit case of karatsuba_multiplication method

    if len(str(a)) == 1 or len(str(b)) == 1:
        return int(a) * int(b)

    # Else, recursively call karatsuba_multiplication

    else:

        # Find the floor of the maximum of mid-point's of the input numbers lengths
        mid = max(len(str(a)), len(str(b)))
        mid2 = mid // 2

        # Find the parameters for computation of terms in karatsuba's algorithm
        anew = int(a) // 10 ** mid2
        bnew = int(a) % 10 ** mid2
        cnew = int(b) // 10 ** mid2
        dnew = int(b) % 10 ** mid2

        # recursive computation of constituent terms in karatsuba algorithm

        term_a = karatsuba_multiplication(bnew, dnew, r)
        term_b = karatsuba_multiplication(anew, cnew, r)
        term_inter_e = karatsuba_multiplication((anew + bnew), (cnew + dnew), r)

        # return the multiplication value using formula in the algorithm, this answer is in base 10

        return term_a + (term_b * 10 ** (2 * mid2)) + ((term_inter_e - term_b - term_a) * 10 ** mid2)


if __name__ == "__main__":
    number1 = sys.argv[1]
    number2 = sys.argv[2]
    base = sys.argv[3]

    # convert the number from base r to base 10
    converted_number1 = baseconvert.base(number1, int(base), 10, string=True)
    converted_number2 = baseconvert.base(number2, int(base), 10, string=True)

    # If base is not 10,convert the product from base r to base 10, else, display product

    product = karatsuba_multiplication(converted_number1, converted_number2, base)
    if 10 != int(base):
        converted_product = baseconvert.base(product, 10, int(base), string=True)
        print("The multiplication of {} and {} in base {} is {}".format(number1, number2, base, converted_product))
    else:
        print("The multiplication of {} and {} in base {} is {}".format(number1, number2, base, product))

