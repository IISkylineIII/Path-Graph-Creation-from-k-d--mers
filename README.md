# Path-Graph-Creation-from-k-d--mers

# Description

This script constructs a path graph from a DNA string by extracting overlapping (k,d)-mers, where k is the length of the substrings and d is the distance between them. Each edge in the graph represents a transition between a prefix and a suffix of the (k,d)-mer. The graph is useful in genome assembly, where the aim is to find paths that reconstruct the original sequence from paired reads.

# Usage
Example

```
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

# Example usage
Text = "TAATGCCATGGGATGTT"
k = 3
d = 1

path_graph = create_path_graph(Text, k, d)
visualize_path_graph(path_graph)
```

Output

TA -> GCC: TAATGCC
AA -> CCA: AATGCCA
AT -> CAT: ATGCCAT
TG -> ATG: TGGGATG
GC -> TGG: GCCATGG
CC -> GGG: CCATGGG
CA -> GGA: CATGGGA
AT -> GAT: ATGGGAT
GG -> TGT: GGGATGT
GG -> GTT: GGATGTT


# Function Descriptions
* create_path_graph(Text, k, d)
Generates a path graph where each edge represents a (k,d)-mer, consisting of a prefix and a suffix. The graph maps pairs of prefixes and suffixes to the corresponding (k,d)-mer.
*  visualize_path_graph(path_graph)
Displays the path graph in a readable format, showing the transition between prefixes and suffixes.

# Applications

* Genome assembly using paired-end reads
* Visualizing the structure of (k,d)-mers in bioinformatics
* Educational purposes for understanding path graphs in sequence reconstruction

# License
* This project is licensed under the MIT License.
