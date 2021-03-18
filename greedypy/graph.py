import json

VERTEX = "vertex"
EDGE = "edge"


class Graph:
    def __init__(self, graph_path):
        self.graph_path = graph_path
        self.vertices = []
        self.edges = {}
        self.graph = ()

    def check_and_add(self, component1, component2=None, c_type=VERTEX):
        if c_type == VERTEX and component1 not in self.vertices:
            self.vertices.append(component1)
        elif (
            c_type == EDGE
            and component1 in self.edges.keys()
            and component2 not in self.edges[component1]
        ):
            self.edges[component1].append(component2)
        elif c_type == EDGE:
            self.edges.update({component1: [component2]})

    def parse_file_content(self, raw_content):
        lines = raw_content.split("\n")
        print("Found ", len(lines), " lines.")
        for line in lines:
            # if line[0] !="p" and line[0]!="c" and line!="c" and line != " ":
            if len(line) != 0:
                words = line.split(" ")
                vert1 = words[1]
                vert2 = words[2]
                self.check_and_add(vert1, VERTEX)
                self.check_and_add(vert2, VERTEX)
                self.check_and_add(vert1, vert2, EDGE)
                self.check_and_add(vert2, vert1, EDGE)
        print(">>>>>>VERTEX")
        print(self.vertices)
        print("----------------------------")
        print("Amount of vertex found : ", len(self.vertices))
        print(">>>>>>EDGES")
        print(json.dumps(self.edges, sort_keys=True, indent=4))
        print("----------------------------")
        suma = sum([len(self.edges[x]) for x in self.vertices])
        print("Amount of edges found : ", suma / 2)

    def build_graph(self):
        with open(self.graph_path) as f:
            content = f.read()
        self.parse_file_content(content)

        self.graph = (self.vertices, self.edges)


anna = Graph("./anna.corr")
anna.build_graph()
