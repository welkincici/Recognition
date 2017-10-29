# Learning log  
### 2017.5.6  
We decide to use python to build the project. It will be based on neural networks and deep learning.  
OPENCV is efficient, but it may a little bit out of date. The recent recognition methods are mentioned above.  
To start our learning, we choose 'Deep Learning' as reference book, and use frame tensorflow and keras to practice.  
### 2017.5.7   
Tensorflow can help us learn some details of deep learning, and Keras is easy to use. Our plan is to study tensorflow first, and learn some about Keras after acquisiting basic deep learning knowledge.   

----  

### 2017.5.8  
Hongli Ni has acquisited a preliminary understanding of Python and is able to develop simple project with Python.   
### 2017.5.11
I start to read the tutorial of tensorflow. I learn several new concepts: tensor, cross-entropy and some algorithms. I am excited, because the tutorial clarifies the approach to develope machine vision in my mind (although just a little).   
The tutorial introduces a program that can distinguish hand-written numbers at the begining. The code is simple and clear: at first, define several vectors representing certain objects or concepts. At second, apply the softmax regression model.At last, use the training data to reduce the cross-entropy, which indicates the cost of the model.    
Emm.. I think I should manage to improve my English writing skills.  
By Hongli  
### 2017.5.12  
Today when I skim through the answers below the topic Tensorflow in zhihu, I meet a suggestion that keras is a better choice for researchers who want to build projects quickly and do not care much about the basic algorithm. I remember that the first program in tensorflow tutorial consists of a lot of mathematical algorithms. I think it is not necessary to acquisite all these algorithms, besides, I am not very interested in them.   
So I decide to change our plan. We learn to use keras first, and try to achieve basic function as quickly as possible.   
### 2017.5.15
Tensorflow & Keras environment configuration done.  
By Holly


### 2017.6.6
Great work! You have got big advances. 
Which operation system do you use, windows or linux? Linux seems to be friendly for deep learning.
By ricky

----   

### 2017.8.1   
Resume updating!   
Get started with tensorflow. Try to get familier with basic components of tensorflow and understand their working process. Following are some important knowledge nodes.   
The most fundamental concepts of tensorflow are tensor and computational graph. The central unit of data in TensorFlow is the tensor, and a computational graph is a series of TensorFlow operations arranged into a graph of nodes.   
A TensorFlow Core program can be seen as consisting of two discrete sections:    
1. Building the computational graph.   
2. Running the computational graph.   

### 2017.8.3  
Learn how to write the simplist machine learning program : Linear Regression.   
In conclusion, a machine learning consists of two parts:   
1. Find symbolic derivatives
2. Change values of variables to minimize( or maximize, in short, to make these number idealize) symbolic derivatives according training data.        
   
Begin learning MNIST   

### 2017.8.4  
Finish MNIST for beginners    
A nice function to determine the loss of a model is called "cross-entropy."
MNIST is the "Hello World" in machine learning. It just a beginning.   
Begin learning MNIST for Experts    

### 2017.8.12   
Lacking of knowledge of CNN makes the learning process somewhat difficult.   
So turn to learn something about CNN. Following are reference materials:   
Wikipedia: Convolutional neural network https://en.wikipedia.org/wiki/Convolutional_neural_network#cite_note-6   
Tensorflow: A Guide to TF Layers: Building a Convolutional Neural Network https://www.tensorflow.org/tutorials/layers   
Tensorflow: Convolutional Neural Networks https://www.tensorflow.org/tutorials/deep_cnn   

### 2017.8.18   
Now let's divide our problem into three parts:    
1. Construct the dataset, and feed it to the model   
2. Design the CNN   
3. Save the training result   

The second part is too difficult for us to complete by ourselves, so we decide to build our model on the base of some successful models, for example: VGG, and train it using our dataset.     
Reference Materials:     
The Keras Blog: https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html (yes, it's Keras Blog, I haven't decide whether to use Keras or Tensorflow yet. I afraid that Keras will be too slow to use in the future product, but it indeed much easier to use than Tensorflow.)     

------

### 2017.8.20
A fantastic material to understand CNN: http://cs231n.github.io/convolutional-networks/   
First try!   
The accuracy arrives 90% for one epoch, I think it is a good result.    
But there are more tests to be done. Our dataset is too small.

### 2017.8.22
The expense of running the VGG16 net is too high, and we turn back to use simple net built by ourselves. Afterall, our goal is pretty easy, so the simple net is probably enough.

### 2017.9.2
Improve the accuracy by expand pictures from 150×150 to 384×384   
We will add more classes in the following days     

------

### 2017.9.3   
The validation accuracy of the model is very poor after adding the third class. We should find approaches to advance our model.    
Our target of the first stage is to bulid a classifier of ten classes whose accuacy is beyond 90%. The further target is visualizing the output of every layer and speed up the model.   
More reference(learning) materials:   
Keras documentation https://keras.io/   
The world in CNN's eye https://keras-cn.readthedocs.io/en/latest/blog/cnn_see_world/   
Zhihu: You need these 14 design mode to improve your CNN https://zhuanlan.zhihu.com/p/26403420   
Tensorflow playground http://playground.tensorflow.org/   
CS 20SI: Tensorflow for Deep Learning Research: http://web.stanford.edu/class/cs20si/index.html   

### 2017.9.23   
Sorry to come back after such a long period of time. I have difficulty in dealing with over-fitting. I tried several method to solve the problem like earlystopping function, add GaussianNoise and expand dataset but they didn't work.    
I think I know too little about the CNN, which make the work of adjusting parameters so difficult and without direction. So I decide to learn CS231N, the stanford university course, to acquisite more knowledge and skills.    

### 2017.10.29   
I have finish CS231N and have build a success net in the base of Mobilenet. The accuracy of ten classes classification is 85%, which still can be improved a lot.    
Mobilenet is developed by Google. It has far less parameters and calculation cost comparing to other nets like VGG16 with a little lose in accuracy so that is likely to be applied in mobile devices.
I am going to enter next stage : detectation.
Paper of Mobilenet :https://arxiv.org/pdf/1704.04861.pdf
