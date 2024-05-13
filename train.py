import tensorflow as tf 
from tensorflow.keras.layers import Dense,Birectional,LSTM
from tensorflow.keras.data.sets import imdb


num_words= 10000 # nombre de mot à utiliser
maxlen =100 # longueur maximale de chaque avis
(x_train,y_train),(x_test, y_test)=imdb.load_data(num_words=num_words)