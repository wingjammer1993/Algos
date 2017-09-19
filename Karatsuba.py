import sys
import baseconvert

def karatsuba_multiplication(a,b,r):
    if len(str(a)) == 1 or len(str(b)) == 1:
        return int(a) * int(b)
    else:
        mid = max(len(str(a)), len(str(b)))
        mid2 = mid // 2

        anew = int(a) // 10 ** mid2
        bnew = int(a) % 10 ** mid2
        cnew = int(b) // 10 ** mid2
        dnew = int(b) % 10 ** mid2

        term_a = karatsuba_multiplication(bnew, dnew, r)
        term_b = karatsuba_multiplication(anew, cnew, r)
        term_inter_e = karatsuba_multiplication((anew + bnew), (cnew + dnew), r)

        return term_a + (term_b * 10 ** (2 * mid2)) + ((term_inter_e - term_b - term_a) * 10 ** mid2)


if __name__ == "__main__":
    number1 = sys.argv[1]
    number2 = sys.argv[2]
    base = sys.argv[3]
    converted_number1 = baseconvert.base(number1, int(base), 10, string=True)
    converted_number2 = baseconvert.base(number2, int(base), 10, string=True)
    # print(converted_number1)
    # print(converted_number2)
    product = karatsuba_multiplication(converted_number1, converted_number2, base)
    if 10 != int(base):
        converted_product = baseconvert.base(product, 10, int(base), string=True)
        print("The multiplication of {} and {} in base {} is {}".format(number1, number2, base, converted_product))
    else:
        print("The multiplication of {} and {} in base {} is {}".format(number1,number2,base,product))

