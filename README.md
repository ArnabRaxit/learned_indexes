## PROJECT DESCRIPTION
There has recently been a lot of excitement about a new proposal https://arxiv.org/abs/1712.01208 from authors at Google: to replace conventional indexing data structures like B-trees and hash maps (as typically used within database systems) by instead fitting a neural network to the dataset. The paper compares such learned indexes against several standard data structures and reports promising results. While learned indexes are an exciting research area, traditional data structures have been optimized for decades. In this project we will investigate the pros and cons of both.


###  Outline of a research proposal
Primary objective is to reproduce results from *Case for learned index* paper
A secondary objective is to model indexing of data as a dimensionality reduction problem. Each data point represents a point in a high dimensional space. Indexing is essentially mapping that data point into a low dimensional space e.g a 3-D space could be: <node, disk, sector>

   

#### Expected outcomes, significance or rationale

   This project will investigate how effective neural network is for learning indexes as inspired by the **Case for learned index** paper. A positive outcome will have an significant impact on design of databases among other things. As GPUs and TPUs become more commonplace in comodity computing equipments, neural nets will be an attractive option to model indexes becuase of their low space requirements.    


