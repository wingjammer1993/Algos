import numpy


def max_probability(a, p, q):
    p_matrix = numpy.empty((len(a), len(a)))
    p_matrix[:] = numpy.float('-inf')

    for i in range(q, p-1, -1):
        for j in range(i, q+1):
            if j == q:
                p_matrix[i][j] = charge(a[i:j+1])
            elif i <= j:
                num = charge(a[i:j+1])
                num_max = numpy.max(p_matrix[j+1])
                p_matrix[i][j] = num*num_max

    return numpy.max(p_matrix[0])


def charge(string):
    d = {'p': 0.9, 'pa': 0.8, 'pan': 0.2, 'pand': 0.01, 'a': 0.5, 'an': 0.9, 'and': 0.7, 'n': 0.2,
                           'nd': 0.6, 'd': 0.9}
    val = 1
    str_n = string
    if isinstance(string, list):
        str_n = ''
        for elem in string:
            str_n = str(str_n) + str(elem)
    if str_n in d:
        val = d[str_n]
    return val


if __name__ == "__main__":
    arr = 'pand'
    prob = max_probability(arr, 0, len(arr)-1)
    print(prob)