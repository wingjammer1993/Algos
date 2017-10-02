from functools import reduce


class SearchGraph:

    def __init__(self, input_graph, start_vertex, list_label):
        self.path = []
        self.path_ways = [0]*(len(list_label)+1)
        self.probability = 0
        self.probability_ways = [0]*(len(list_label))
        self.input_graph = input_graph
        self.start_vertex = start_vertex
        self.list_label = list_label
        self.current_index = 0

    # This method will call the internal search_sequence method and return path
    # If path is present, it returns the same
    # Else it returns 'NO'

    def return_path(self):
        length = len(self.list_label)
        self.search_sequence(self.input_graph, self.start_vertex, self.list_label, self.current_index)
        if len(self.path) == length + 1:
            return self.path
        else:
            return 'NO'

    # This method returns the first path which matches the input observation sequence.
    # Else it returns a partial matching path

    def search_sequence(self, input_graph, start_vertex, list_label, current_index):

        if not list_label:
            self.path_ways[current_index] = start_vertex
            probability_value = reduce(lambda x, y: x * y, self.probability_ways, 1)
            if probability_value > self.probability:
                self.probability = probability_value
                self.path = list(self.path_ways)
            current_index = current_index - 1
            return

        for child, symbol, probability in input_graph[start_vertex]:
            new_list = list(list_label)
            if symbol == new_list[0]:
                new_list.remove(symbol)
                self.path_ways[current_index] = start_vertex
                self.probability_ways[current_index] = probability
                self.search_sequence(input_graph, child, new_list, current_index+1)
                print(current_index)


if __name__ == "__main__":
    graph = {'A': {('B', 'a', 0.1), ('C', 'a', 0.2)},
             'B': {('D', 'b', 0.3), ('C', 'f', 0.5), ('E', 'b', 0.7)},
             'C': {('D', 'f', 0.3), ('E', 'b', 0.2)},
             'D': {('E', 'c', 0.5)},
             'E': {('B', 'c', 0.4)}}
    o = ['a', 'b', 'c']
    s = SearchGraph(graph, 'A', o)
    path = s.return_path()
    probability_s = s.probability
    print(probability_s)
    print(path)

