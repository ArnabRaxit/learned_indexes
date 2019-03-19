## PROJECT DESCRIPTION
There has recently been a lot of excitement about a new proposal https://arxiv.org/abs/1712.01208 from authors at Google: to replace conventional indexing data structures like B-trees and hash maps (as typically used within database systems) by instead fitting a neural network to the dataset. The paper compares such learned indexes against several standard data structures and reports promising results. While learned indexes are an exciting research area, traditional data structures have been optimized for decades. In this project we will investigate the pros and cons of both.


###  Outline of a research proposal
Primary objective is to reproduce results from *Case for learned index* paper within resonable limits.
A sufficiently large dataset will be attempted to be indexed using the learned index neural network and if the recource consuption for training the neural network is too high for a single machine eithr [model parallelism or data parallelism](https://blog.skymind.ai/distributed-deep-learning-part-1-an-introduction-to-distributed-training-of-neural-networks/) technique will be used to succesfully complete the training.
A secondary objective is to explore how a learned index can be applied to a global index where a dataset is stored across multiple nodes e.g a hadoop based system.


#### Methodology
   Various machine learning and AI libraries and tools like Tensorflow, pytorch, Keras, Caffee will be used codify the algorithm outlined in the paper. Traning will be run on multiple datasets to learn the index. Initially the entire dataset will be loaded to memory and it wil be treated as a contigous array of key_value pairs. Where "key" is the index i.e in case of a array in memory its simply the index starting at 0. The "value" could either be the record itself or a pointer to the record. 
   The same datasets will be indexed using a C++ implemnetation of B-tree.
   
   Once the indexing is completed (using both B-tree and learned index) a search and retrival of random values will be carried out. Data retrival will involve interrogating the index for the approximate position of the value and then doing a binray search from that point.
   Metrics ( time and space) will be collected for both the B-tree and learned index methods and a comparitive study will be done.
   
   Once the above has been achived for a relatively small dataset (~20K records) a scaled up version will be attempted in order to establish the point where [model parallelism or data parallelism](https://blog.skymind.ai/distributed-deep-learning-part-1-an-introduction-to-distributed-training-of-neural-networks/) will be required to complete training. Apache Spark is a potential candidate which may be used to [distribute the neural network training](https://towardsdatascience.com/deep-learning-with-apache-spark-part-2-2a2938a36d35).
   This project will require access to relevant literature , mostly in reference to the **Case for learned index** paper. Google scholar is a great place to look for literature and will be utilised. Open source software like a database, B-tree implementations, Neural net framework like pytorch or tensorflow will potentially be used. Programming language like C, Java, Python or Go may be used.
   
   Finally, the code developed so far will also be attempted on GPU(s) to measure the improvement in training time and if distributed parallel GPUs can be used to further speed up training.
   

#### Expected outcomes, significance or rationale

   This project will investigate how effective neural network is for learning indexes as inspired by the **Case for learned index** paper especially for large datasets which cannot be trained on a single node. A positive outcome will have an significant impact on design of databases among other things. As GPUs and TPUs become more commonplace in comodity computing equipments, neural nets will be an attractive option to model indexes becuase of their low space requirements.    


#### Timetable
A tentative timeline for the project to be carried out over 2 semesters is below:

| week due | Task |
| :---------- | :------ |
| week 2 |  Deep dive into B-tree implementations |
| *** | _Design and Implement machine learning algorithms to learn indexs_|
| week 3  |  with neural nets |
| week 5 |  with dimensionality reduction techniques |
| week 7 |  Benchmarking these algorithms on a dataset |
| week 10 |  Integrate some of the algorithms into an open source database code. |
| *** |  _Analyse performance of the database from various angles_ |
| week 11 |   during data retrieval |
| week 12 |   during data insertion |
| week 12 |   Final report |
