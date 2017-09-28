
a = [1,1,1,2,2,2,3,3,3]


def linear_search(a):
    for index, elem in enumerate(a):
        if index == a[index]:
            return index;
    else:
        return -1;

if __name__ == "__main__":
    answer = linear_search(a)
    print(answer)