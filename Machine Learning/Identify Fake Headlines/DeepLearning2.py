import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #disables tf telling me i have wrong gpu
import tensorflow as tf
from tensorflow import keras

#loading some data downloaded from kaggle
import json

datastore = [json.loads(line) for line in open('sarcasm.json','r')]

sentences = []
labels = []
urls = []

for item in datastore:
	sentences.append(item['headline'])
	labels.append(item['is_sarcastic'])
	urls.append(item['article_link'])

#doing the previous work of tokenizing each sentence
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


vocab_size = 50000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = 20000

#we lay out sentences to be training as well as to be validating
training_sentences = sentences[:training_size]
testing_sentences = sentences[training_size:]
training_labels = labels[:training_size]
testing_labels = labels[training_size:]

#we tokenize only the sentences that we are training with or else we have data leakage
tokenizer = Tokenizer(num_words = vocab_size,oov_token = oov_tok)
tokenizer.fit_on_texts(training_sentences)

word_index = tokenizer.word_index

#putting the training/testing sentences into sequences via the work_index, and then padding them so they are all equal length
training_sequences = tokenizer.texts_to_sequences(training_sentences)
training_padded = pad_sequences(training_sequences,padding = padding_type,maxlen=max_length,truncating=trunc_type)

testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
testing_padded = pad_sequences(testing_sequences, padding = padding_type,maxlen=max_length,truncating=trunc_type)

#apparently is necessary to not through an error in tf 2.X
import numpy as np
training_padded = np.array(training_padded)
training_labels = np.array(training_labels)
testing_padded = np.array(testing_padded)
testing_labels = np.array(testing_labels)

#defines the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

#
model.compile(loss = 'binary_crossentropy', optimizer ='adam', metrics = ['accuracy'])

#number of times the data gets shown to the nueral network, more epochs = more trained
num_epochs = 30
#actually goes through and trains the model. Also tells how accurate it is by comparing to validation data
history = model.fit(training_padded, training_labels, epochs=num_epochs, validation_data=(testing_padded, testing_labels), verbose=2)


#can test the model on new sentences after it has been trained

#sentence = ["I can't wait to be your friend",
#			'the weather today is bright and sunny']

#sequences = tokenizer.texts_to_sequences(sentence)

#padded = pad_sequences(sequences,maxlen = max_length, padding=padding_type, truncating=trunc_type)

#print(model.predict(padded))

#VERY COOL STUFF!!!!!!