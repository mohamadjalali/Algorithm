class Graph:
    def __init__(self):
        self.adj_list = {}

    
    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} : {self.adj_list[vertex]}")


    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False


    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False


    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            if self.adj_list[vertex] == []:
                del self.adj_list[vertex]
            else:
                for i in self.adj_list[vertex]:
                    target = self.adj_list[i]
                    target.remove(vertex)
                del self.adj_list[vertex]
                return True
            return False

if __name__ == "__main__":
    graph = Graph()

    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')

    graph.add_edge('A', 'B')
    graph.add_edge('C', 'A')
    graph.add_edge('A', 'D')
    graph.add_edge('D', 'C')
    graph.add_edge('D', 'B')

    graph.remove_vertex('D')
    graph.print_graph()
