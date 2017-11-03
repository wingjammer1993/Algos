
def find_majority(a):
    current = a[0]
    count = 0
    for elem in a:

        if count == 0:
            current = elem
            count = 1
        elif current == elem:
            count = count + 1
        else:
            count = count - 1

    majority_count = len(a)/2
    current_count = 0
    for elem in a:
        if elem == current:
            current_count = current_count + 1

    if current_count > majority_count:
        return current
    else:
        return 'No Majority'


if __name__ == "__main__":
    question = ['p', 'p', 'p', 'p', 'p', 'd', 'd', 'd', 'd', 'p']
    win = find_majority(question)
    print(win)