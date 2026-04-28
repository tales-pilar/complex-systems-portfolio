import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def generate_networks(n=100):
    er = nx.erdos_renyi_graph(n=n, p=0.05, seed=42)
    ba = nx.barabasi_albert_graph(n=n, m=2, seed=42)
    return er, ba


def compute_metrics(G):
    avg_degree = np.mean([d for _, d in G.degree()])
    clustering = nx.average_clustering(G)
    largest_cc = len(max(nx.connected_components(G), key=len)) / G.number_of_nodes()
    return avg_degree, clustering, largest_cc


def plot_network(G, title, filename):
    plt.figure(figsize=(6, 5))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, node_size=40)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()


def plot_degree_distribution(G, title, filename):
    degrees = [d for _, d in G.degree()]
    plt.figure(figsize=(6, 4))
    plt.hist(degrees, bins=15)
    plt.title(title)
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()


if __name__ == "__main__":
    er, ba = generate_networks()

    er_metrics = compute_metrics(er)
    ba_metrics = compute_metrics(ba)

    print("Erdős–Rényi metrics:")
    print(f"Average degree: {er_metrics[0]:.4f}")
    print(f"Clustering coefficient: {er_metrics[1]:.4f}")
    print(f"Largest component fraction: {er_metrics[2]:.4f}")
    print()
    print("Barabási–Albert metrics:")
    print(f"Average degree: {ba_metrics[0]:.4f}")
    print(f"Clustering coefficient: {ba_metrics[1]:.4f}")
    print(f"Largest component fraction: {ba_metrics[2]:.4f}")

    plot_network(er, "Erdős–Rényi Network", "er_network.png")
    plot_network(ba, "Barabási–Albert Scale-Free Network", "ba_network.png")

    plot_degree_distribution(er, "ER Degree Distribution", "er_degree_distribution.png")
    plot_degree_distribution(ba, "BA Degree Distribution", "ba_degree_distribution.png")
