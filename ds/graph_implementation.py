class GRAPH:
    def __init__(self, edges):

        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=None):

        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            raise Exception("THE START NODE IS INVALID :( ")
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_least_stop_path(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            raise Exception("THE START NODE IS INVALID :( ")
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_least_stop_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path



if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    route_graph = GRAPH(routes)
    print(route_graph.get_least_stop_path("Mumbai", "New York"))
