## PROJECT DESCRIPTION
There has recently been a lot of excitement about a new proposal https://arxiv.org/abs/1712.01208 from authors at Google: to replace conventional indexing data structures like B-trees and hash maps (as typically used within database systems) by instead fitting a neural network to the dataset. The paper compares such learned indexes against several standard data structures and reports promising results. While learned indexes are an exciting research area, traditional data structures have been optimized for decades. In this project we will investigate the pros and cons of both.


###  Outline of a research proposal
Primary object is to reproduce results from *Case for learned index* paper
A secondary objective is to model indexing of data as a dimensionality reduction problem.


#### Methodology
   A relatively modern database such as Apache derby will be choosen as a candidate whose traditional indexing algorithms will be replaced with machine learning algorithms. The reason for choosing a relatively mordern database is that it will carry less legacy code which will help avoiding distractions and cutting to the chase. Various machine learning algorithms mostly neural networks but also some dimensionaity reduction techniques will be used to model the indexes.
 
   This project will require access to relevant literature , mostly in reference to the **Case for learned index** paper. Google scholar is a great place to look for literature and will be utilised. There could be a need to use specialised processors like GPUs which are great for repetative tasks like matrix multiplications essential for training neural nets. Open source software like a database, B-tree implementations, Neural net framework like pytorch or tensorflow will potentially be used. Programming language like C, Java, Python or Go may be used.
   

#### Expected outcomes, significance or rationale

   This project will investigate how effective neural network is for learning indexes as inspired by the **Case for learned index** paper. A positive outcome will have an significant impact on design of databases among other things. As GPUs and TPUs become more commonplace in comodity computing equipments, neural nets will be an attractive option to model indexes becuase of their low space requirements.    


#### Timetable
| week due | Task |
| :---------- | :------ |
| week 3 |  Deep dive into B-tree implementations |
| *** | _Design and Implement machine learning algorithms to learn indexs_|
| week 6  |  with neural nets |
| week 10 |  with dimensionality reduction techniques |
| week 15 |  Benchmarking these algorithms on a dataset |
| week 20 |  Integrate some of the algorithms into an open source database code. |
| *** |  _Analyse performance of the database from various angles_ |
| week 22 |   during data retrieval |
| week 24 |   during data insertion |
| week 24 |   Final report |
