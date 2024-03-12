class graph:
    def __init__(self):
        self.adjacency_list = {}
    def insert_vertex(self,vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    def insert_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
        else:
            self.adjacency_list[vertex1] = [vertex2]

        if vertex2 in self.adjacency_list:
            self.adjacency_list[vertex2].append(vertex1)
        else:
            self.adjacency_list[vertex2] = [vertex1]

    def display(self):
        for vertex,adjacent in self.adjacency_list:
            print(vertex,"-> " ,adjacent)

    def delete(self,vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
        for v in self.adjacency_list:
            if vertex in self.adjacency_list[v]:
                self.adjacency_list[v].remove(vertex)


    def depth_first_search(self,start_vertex):
        visited = set()
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            if vertex not in vertex:
                vertex.add(vertex)
                for neighbour in self.adjacency_list.get(vertex,[]):
                    if neighbour not in visited:
                        stack.append(neighbour)
        return visited

    def breadth_first_search(self,start_vertex):
        visited = set()
        queue = [start_vertex]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                for neighbour in self.adjacency_list.get(vertex,[]):
                    if neighbour not in visited:
                        queue.append(neighbour)
        return visited