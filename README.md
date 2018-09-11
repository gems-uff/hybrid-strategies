Hybrid Strategies
=================

Copyright (c) 2018 Universidade Federal Fluminense (UFF).

A hybrid search strategy is an approach that combines database search and snowballing to conduct a Systematic Literature Review (SLR) in Software Engineering.

The goal of this work is to propose and evaluate hybrid search strategies combining searching in several databases or in a specific digital library with parallel or sequential backward and forward snowballing. 

The proposed hybrid search strategies were applied to three previously published SLRs that adopted database searches and snowballing. 
For this, we used the [Snowballing Tool](https://github.com/JoaoFelipe/snowballing) developed by Joao Felipe Pimentel in Python. Additionally, we developed scripts to simulate the proposed hybrid search strategies. 

We evaluated whether the strategys are able to retrieve the selected papers with lower effort in terms of the number of analyzed papers 
(Precision), whether they are able to retrieve all papers that were selected in the published SLR (Recall) and we used the harmonic mean between Precision and Recall (F-measure) to analyses the combined results.

To improve understanding, we adopted visualizations to represent the strategies flow, the citation matrix, citation graph, and the steps to find papers through backward and forward snowballing. 

This work is part of Erica Mourao master thesis.

Experiments
-----------

| Experiment 1 | Experiment 2 | Experiment 3 |
|   :---:      |     :---:    |     :---:    |
| [Hybrid Strategies](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_1/notebooks/1_HybridStrategies.ipynb) | [Hybrid Strategies](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_2/notebooks/1_HybridStrategies.ipynb) | [Hybrid Strategies](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_3/notebooks/1_HybridStrategies.ipynb)
| [Citation Matrix](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_1/notebooks/2_CitationMatrix.ipynb) | [Citation Matrix](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_2/notebooks/2_CitationMatrix.ipynb) | [Citation Matrix](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_3/notebooks/2_CitationMatrix.ipynb)
| [Citation Graph](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_1/notebooks/3_CitationGraph.ipynb) | [Citation Graph](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_2/notebooks/3_CitationGraph.ipynb) | [Citation Graph](https://github.com/gems-uff/hybrid-strategies/blob/master/experiments/experiment_3/notebooks/3_CitationGraph.ipynb)
| [Report](https://github.com/gems-uff/hybrid-strategies/tree/master/experiments/experiment_1/documents) |[Report](https://github.com/gems-uff/hybrid-strategies/tree/master/experiments/experiment_2/documents) | [Report](https://github.com/gems-uff/hybrid-strategies/tree/master/experiments/experiment_3/documents)

Publications
------------

- [Mourão, E., Kalinowski, M., Murta, L., Mendes, E., & Wohlin, C.. Investigating the use of a hybrid search strategy for systematic reviews. ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM), 2017 (pp. 193-198).](https://ieeexplore.ieee.org/document/8170102/)

Main Team
---------

- Erica Mourao (UFF, Brazil)
- Joao Felipe Pimentel (UFF, Brazil)
- Leonardo Murta (UFF, Brazil)
- Marcos Kalinowski (PUC-Rio, Brazil)

Collaborators
-------------

- Emilia Mendes (BTH, Sweden)
- Claes Wohlin (BTH, Sweden)

Included Software
-----------------

- [Snowballing Tool](https://github.com/JoaoFelipe/snowballing)

Programming Language
--------------------

- Python

Acknowledgements
----------------

We would like to thank CAPES, CNPq and FAPERJ for partially supporting this work.

License Terms
-------------

The MIT License (MIT)

Copyright (c) 2018 Universidade Federal Fluminense (UFF).

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
