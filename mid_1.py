
def find_winner(arr, p, mid, q, left_w, left_c, right_w, right_c):
    if left_w == right_w:
        return left_w, left_c+right_c

    count_l = 0
    count_r = 0
    if left_w != right_c:
        for elem in arr[mid+1:q+1]:
            if elem == left_w:
                count_l = count_l + 1

        for elem in arr[p:mid+1]:
            if elem == right_w:
                count_r = count_r + 1

    length = (len(arr[p:q]) + 1) / 2
    if left_c + count_l > length:
        return left_w, left_c + count_l

    elif right_c + count_r > length:
        return right_w, right_c + count_r

    else:
        return None, 0


def find_majority(a, p, q):
    if p == q:
        return a[p], 1

    if p < q:
        mid = p + (q - p) // 2
        L_w, L_c = find_majority(a, p, mid)
        R_w, R_c = find_majority(a, mid+1, q)
        return find_winner(a, p, mid, q, L_w, L_c, R_w, R_c)


if __name__ == "__main__":
    question = ['p', 'c', 'd', 'd', 'c', 'd', 'p', 'd', 'd']
    win, count = find_majority(question, 0, len(question)-1)
    print(win)







