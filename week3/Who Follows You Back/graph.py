class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, node_a, node_b):
        if node_b not in self.edges.keys():
            self.edges[node_b] = set()
        if node_a not in self.edges.keys():
            self.edges[node_a] = set()
            self.edges[node_a].add(node_b)
        else:
            self.edges[node_a].add(node_b)

    def get_neighbours_for(self, node):
        try:
            return self.edges[node]
        except:
            print("{} is not in the graph".format(node))

    def dfs(self, node_a):
        visited, stack = set(), [node_a]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(self.get_neighbours_for(node))
        return visited

    def path_between(self, node_a, node_b):
        return node_b in self.dfs(node_a)

    def __str__(self):
        string = ""
        for key in self.edges.keys():
            string += "{} - {}\n".format(key, self.edges[key])
        return string

