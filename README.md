# Hybrid Strategies


# About

A hybrid search strategy is an approach that combines database search and snowballing to conduct the Systematic Literature Reviews (SLR) in Software Engineering.

The goal of this work is to propose and evaluate hybrid search strategies combining searching in several database searches or in a specific digital library with parallel or sequential backward and forward snowballing. 

The proposed hybrid search strategies were applied to three previously published SLRs that adopted database searches and snowballing. 
For this, we used the [Snowballing Tool](https://github.com/JoaoFelipe/snowballing) developed by Joao Felipe Pimentel in Python language and we developed a new code to provide different simulations of hybrid search strategies. 

We evaluate whether the strategy is able to retrieve the selected papers with lower effort in terms of the number of analyzed papers 
(Precision), if it is able to retrieve all papers that were selected in the published SLR that conducted searches on databases and snowballing (Recall) and we used the harmonic mean between Precision and Recall (F-measure) to analyses the results.

To improve understanding we represent the strategies flow, the citation matrix, citation graph, and the steps to find papers through 
backward and forward snowballing providing visualization and data for analysis. 

In summary, this work is part of Erica Mourao Master Science Thesis.


# Experiments
| Experiment 1 | Experiment 2 | Experiment 3 |
|   :---:      |     :---:    |     :---:    |
| [Hybrid Strategies](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_1/notebooks/1_HybridStrategies.ipynb) | [Hybrid Strategies](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_2/notebooks/1_HybridStrategies.ipynb) | [Hybrid Strategies](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_3/notebooks/1_HybridStrategies.ipynb)
| [Citation Matrix](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_1/notebooks/2_CitationMatrix.ipynb) | [Citation Matrix](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_2/notebooks/2_CitationMatrix.ipynb) | [Citation Matrix](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_3/notebooks/2_CitationMatrix.ipynb)
| [Citation Graph](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_1/notebooks/3_CitationGraph.ipynb) | [Citation Graph](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_2/notebooks/3_CitationGraph.ipynb) | [Citation Graph](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_3/notebooks/3_CitationGraph.ipynb)
| [Report](https://github.com/gems-uff/hybrid-strategies/tree/master/experiments/experiment_1/documents) |[Report](https://github.com/gems-uff/hybrid-strategies/tree/master/experiments/experiment_2/documents) | [Report](https://github.com/gems-uff/hybrid-strategies/tree/master/experiments/experiment_3/documents)


# Publications
- [Investigating the Use of a Hybrid Search Strategy for Systematic Reviews](https://ieeexplore.ieee.org/document/8170102/)
- [Guidelines for Snowballing in Systematic Literature Studies and a Replication in Software Engineering](https://dl.acm.org/citation.cfm?id=2601268)


# Team
- Erica Mourao (UFF)
- Joao Felipe Pimentel (UFF)
- Leonardo Murta (UFF)

Collaborator
- Marcos Kalinowski (PUC-Rio)

# Software
- [Snowballing Tool](https://github.com/JoaoFelipe/snowballing)


# Programming Language
- Python


# License
Copyright (c) 2017 Universidade Federal Fluminense (UFF)
