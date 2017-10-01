
class SearchGraph:

    def __init__(self):
        self.path = []

    # This method will call the internal search_sequence method and return path
    # If path is present, it returns the same
    # Else it returns 'NO'

    def return_path(self, input_graph, start_vertex, list_label):
        length = len(list_label)
        self.search_sequence(input_graph, start_vertex, list_label)
        if len(self.path) == length + 1:
            return self.path
        else:
            return 'NO'

    # This method returns the first path which matches the input observation sequence.
    # Else it returns a partial matching path

    def search_sequence(self, input_graph, start_vertex, list_label):

        if not list_label:
            self.path.append(start_vertex)
            return

        for child, symbol in input_graph[start_vertex]:
            if symbol == list_label[0]:
                list_label.remove(symbol)
                self.path.append(start_vertex)
                self.search_sequence(input_graph, child, list_label)
                break


if __name__ == "__main__":
    graph = {'A': {('B', 'a'), ('C', 'b')},
             'B': {('D', 'b'), ('C', 'b')},
             'C': {('D', 'a'), ('E', 'd')},
             'D': {('E', 'e')},
             'E': set()}

    s = SearchGraph()
    o = ['a', 'b']
    path = s.return_path(graph, 'A', o)
    print(path)

