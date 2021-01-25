#Determine if an article is fake news or not
#practice on my own
#data from kaggle
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #disables tf telling me i have wrong gpu
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd

sentences = pd.read_csv('TorF.csv').title
labels = pd.read_csv('TorF.csv').label

vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = 10000

#Defining our data
#trying to make an even split between true and false headlines
training_sentences1 = sentences[:training_size]
training_sentences2 = sentences[2*training_size:]
training_sentences = pd.concat([training_sentences1,training_sentences2])

testing_sentences = sentences[training_size:2*training_size]

training_labels1 = labels[:training_size]
training_labels2 = labels[2*training_size:]
training_labels = pd.concat([training_labels1,training_labels2])

testing_labels = labels[training_size:2*training_size]

#doing the previous work of tokenizing each sentence
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(num_words = vocab_size ,oov_token = oov_tok)
tokenizer.fit_on_texts(training_sentences)

word_index = tokenizer.word_index


#putting sentences into sequences and then padding them to be equal length
training_sequences = tokenizer.texts_to_sequences(training_sentences)
training_padded = pad_sequences(training_sequences, padding = padding_type, maxlen = max_length, truncating = trunc_type)

testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
testing_padded = pad_sequences(testing_sequences, padding = padding_type, maxlen = max_length, truncating = trunc_type)

#need to put so it runs properly
import numpy as np
training_padded = np.array(training_padded)
training_labels = np.array(training_labels)
testing_padded = np.array(testing_padded)
testing_labels = np.array(testing_labels)

#define the model
model = tf.keras.Sequential([
		tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length = max_length),
		tf.keras.layers.GlobalAveragePooling1D(),
		tf.keras.layers.Dense(24, activation = 'relu'),
		tf.keras.layers.Dense(1,activation = 'sigmoid')
	])
model.compile(loss = 'binary_crossentropy', optimizer ='adam', metrics = ['accuracy'])

num_epochs = 5

history = model.fit(training_padded, training_labels, epochs = num_epochs, validation_data = (testing_padded, testing_labels), verbose = 2)



sentence = ["Republican leaders claim new yorkers will greet us millitary as liberators"]

sequences = tokenizer.texts_to_sequences(sentence)

padded = pad_sequences(sequences,maxlen = max_length, padding=padding_type, truncating=trunc_type)

print(model.predict(padded))