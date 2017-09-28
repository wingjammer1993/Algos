
f = [-1,-2,2,39,53,76,340,876,678]

# Binary Search Algorithm
# param1 = input array which contains values if f(x)
# param2 = start index of array
# param3 = end index of array

def binary_search(f, p, r):

    if r > 0:
        # Find the floor of the mid-point of array bounds
        mid = p+(r-p)//2
        x = f[mid]

        # If mid > x, since the array is sorted in ascending order
        # the value of mid is already greater than f(mid),
        # so we must search for elem,to the right of middle value.
        if mid > x:
            return binary_search(f, mid+1, r)

        # If mid < x, since the array is sorted in ascending order
        # the value of mid is less than f(mid), so we
        # must search for elem to the left of middle value.
        if mid < x:
            return binary_search(f, p, mid-1)

        # elem has been found
        if mid == x:
            return mid
    else:
        return -1




if __name__ == "__main__":
    num1 = 0
    num2 = 8
    middle = binary_search(f, num1, num2)
    print(middle)
