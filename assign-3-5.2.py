import numpy


# Method to find the path of the required sequence in the graph

def find_path(i_graph, start_ver, req_seq):
    a = create_a(i_graph)
    b = create_b(i_graph, start_ver, req_seq)
    pie_1 = [0]*len(i_graph.keys())
    keys = list(i_graph.keys())
    start_idx = keys.index(start_ver)
    pie_1[start_idx] = 1
    answer_path = viterbi_decode(req_seq, keys, a, b, pie_1)
    return answer_path

# Method to create the transition probability matrix for viterbi algorithm

def create_a(ii_graph):
    keys = list(ii_graph.keys())
    a = numpy.zeros((len(ii_graph.keys()), len(ii_graph.keys())))
    for parent in ii_graph:
        for child, label, probability in ii_graph[parent]:
            row = keys.index(parent)
            col = keys.index(child)
            a[row][col] = 1/{k: sum(1 for x in v if x) for k, v in ii_graph.items()}[parent]
    return a

# Method to create the emission probability matrix for viterbi

def create_b(ii_graph, start_ver, req_seq):
    keys = list(ii_graph.keys())
    b = numpy.zeros((len(ii_graph.keys()), len(req_seq)+1))
    start_idx = keys.index(start_ver)
    b[start_idx][0] = 1
    for parent in ii_graph:
        for child, label, probability in ii_graph[parent]:
            if label in req_seq:
                row = keys.index(child)
                col = req_seq.index(label)+1
                b[row][col] = probability
    return b

# Viterbi decoding algorithm


def viterbi_decode(observation_sequence, state_sequence, a, b, pie_1):

    observation_sequence.insert(0, '<s>')
    rows = len(state_sequence)
    columns = len(observation_sequence)
    viterbi = numpy.zeros((rows, columns))
    backtrace = numpy.zeros((rows, columns))
    best_path = numpy.zeros(columns)

    # Initialization - we fill the first column with first column of viterbi trellis

    for s, state in enumerate(state_sequence):
            viterbi[s][0] = pie_1[s]*b[s][0]
            backtrace[s][0] = 0

    # Recursion - we will fill the remaining columns in the state chart

    for t, observation in enumerate(observation_sequence):
        if t != 0:
            for s, state in enumerate(state_sequence):
                func = []
                func_max = []
                for s_iter, state_i in enumerate(state_sequence):
                    v1 = viterbi[s_iter][t-1]
                    v2 = a[s_iter][s]
                    v3 = b[s][t]
                    func.append(viterbi[s_iter][t-1]*a[s_iter][s]*b[s][t])
                    func_max.append(viterbi[s_iter][t - 1] * a[s_iter][s])
                viterbi[s][t] = numpy.amax(func)
                backtrace[s][t] = numpy.argmax(func_max)

    # Termination - we will fill the end column of the trellis

    end_col = len(observation_sequence) - 1
    func_max = []
    for s_iter, state_i in enumerate(state_sequence):
        v1 = viterbi[s_iter][end_col]
        v2 = 1
        func_max.append(viterbi[s_iter][end_col] * 1)

    best_score = numpy.amax(func_max)
    start_backtrace = numpy.argmax(func_max)

    # Backtracking to find the most probable path

    best_path[end_col] = start_backtrace
    for col in range(end_col-1, -1, -1):
        use_index = int(best_path[col+1])
        best_path[col] = backtrace[use_index][col+1]

    answer_string = []
    for index in range(0, len(observation_sequence), 1):
        tag = best_path[int(index)]
        answer_string.append(state_sequence[int(tag)])

    # Check for validity of result

    summation = numpy.sum(viterbi, axis=0)
    if 0 in summation:
        answer_string = 'NO'

    return answer_string


if __name__ == "__main__":
    graph = {'A': {('B', 'o1', 1), ('C', 'o2', 1)},
             'B': {('D', 'o2', 0.5), ('C', 'o2', 0.4), ('E', 'o2', 0.1)},
             'C': {('E', 'o3', 0.6), ('D', 'o3', 0.4)},
             'D': {('F', 'o1', 1)},
             'E': {('F', 'o1', 1)},
             'F': set()}

    start_vertex = 'A'
    obs = ['o1', 'o2']
    path = find_path(graph, start_vertex, obs)
    print(path)

