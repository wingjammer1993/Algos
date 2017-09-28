
f = [12, 11, 10, 9, 8, -9887, -122203, -1111011, -111112011]

# Binary Search Algorithm
# param1 = input array which contains values if f(x)
# param2 = start index of array
# param3 = end index of array

def binary_search(f, p, r):

    if r > 0:
        # Find the floor of the mid-point of array bounds
        mid = p+(r-p)//2
        x = f[mid]

        # elem has been found
        if p == r or x == 0:
            return mid

        # If 0 > x, since the function is strictly decreasing i.e f(i) > f(i+1)
        # the values of x are already less than 0 at mid, so we must search for min n
        # to the left of middle value.
        if 0 > x:
            return binary_search(f, p, mid)

        # If 0 < x, since the function is strictly decreasing i.e f(i) > f(i+1)
        # the values of x are greater 0 at mid, so we must search for elem
        # to the right of middle value.
        if 0 < x:
            return binary_search(f, mid+1, r)


    else:
        return -1




if __name__ == "__main__":
    num1 = 0
    num2 = 8
    element = 0
    middle = binary_search(f, num1, num2)
    print(middle)
