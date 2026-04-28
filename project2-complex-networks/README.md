# Network Structure and Emergence: A Comparative Analysis of Random and Scale-Free Networks

This project is part of a broader portfolio on complex systems focused on nonlinear dynamics, network structure, and data-driven analysis.

---

## Overview

This project investigates how different network generation mechanisms give rise to distinct global structures. By comparing Erdős–Rényi random graphs and Barabási–Albert scale-free networks, we analyze how local connection rules influence macroscopic organization.

---

## Key Scientific Takeaway
> Global network structure is not imposed but emerges from simple local rules. Preferential attachment generates heterogeneous, hub-dominated topologies, whereas random linking produces homogeneous connectivity patterns.

---

## Scientific Motivation

In complex systems, the structure of interactions plays a central role in determining system behavior. Many real-world systems — including social, technological, and biological networks — exhibit non-random connectivity patterns, making it essential to understand how such structures arise.

---

## Research Question

How do different network formation mechanisms influence degree distribution, connectivity patterns, and the emergence of structural heterogeneity?

---

## Models

- **Erdős–Rényi (Random Graph)**  
  Uniform probability of connection between nodes  

- **Barabási–Albert (Scale-Free Network)**  
  Growth with preferential attachment ("rich-get-richer" mechanism)  

---

## Methods

- Generation of networks with equal size  
- Computation of structural metrics:
  - Average degree  
  - Clustering coefficient  
  - Largest connected component  
- Degree distribution analysis (log-scale)

---

## Results

- Random networks exhibit narrow, approximately Poisson degree distributions  
- Scale-free networks display heavy-tailed distributions  
- Hub formation emerges naturally under preferential attachment  

---

## Visual Results

### Degree Distribution
![Degree Distribution](images/degree_distribution.png)

### Random Network
![Random Network](images/random_network.png)

### Scale-Free Network
![Scale-Free Network](images/scale_free_network.png)

---

## Interpretation

The results demonstrate that network topology is highly sensitive to generative mechanisms. Scale-free networks exhibit strong structural heterogeneity, which has implications for robustness, vulnerability, and information flow.

---

## Relevance to Complex Systems

This project highlights how **structure emerges from simple rules**, complementing the dynamical perspective explored in Project 1.

---

## Limitations and Future Work

- Static network analysis only  
- No dynamical processes (diffusion, contagion, resilience)  
- Future extensions:
  - Small-world networks  
  - Network dynamics  
  - Robustness under targeted attacks  
