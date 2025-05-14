def create_path_graph(Text, k, d):
    path_graph = {}
    num_edges = len(Text) - (k + d + k) + 1

    for i in range(num_edges):
        kmer = Text[i:i + k + k + d]
        prefix = kmer[:k - 1]
        suffix = kmer[k + 1:]
        path_graph[(prefix, suffix)] = kmer

    return path_graph

def visualize_path_graph(path_graph):
    for edge, kmer in path_graph.items():
        prefix, suffix = edge
        print(f"{prefix} -> {suffix}: {kmer}")

Text = "TAATGCCATGGGATGTT"
k = 3
d = 1

path_graph = create_path_graph(Text, k, d)
visualize_path_graph(path_graph)
