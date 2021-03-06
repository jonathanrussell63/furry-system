#recurrent neural networks
#LSTM = long-short-term memory
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '4' #disables tf telling me i have wrong gpu
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd


from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer()
data = open('poems.txt').read()
corpus = data.lower().split('\n')


tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index)+1


input_sequences = []

for line in corpus:
	token_list = tokenizer.texts_to_sequences([line])[0]
	for i in range(1,len(token_list)):
		n_gram_sequence = token_list[:i+1]
		input_sequences.append(n_gram_sequence)


max_sequence_len = max([len(x) for x in input_sequences])


input_sequences = np.array(pad_sequences(input_sequences, maxlen = max_sequence_len, padding = 'pre'))


xs = input_sequences[:,:-1]
labels = input_sequences[:,-1]
ys = tf.keras.utils.to_categorical(labels, num_classes= total_words)


from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
#The model has nodes that feed the next node, 64,32 represent the length of the context respectively
model = tf.keras.Sequential()
model.add(Embedding(total_words, 240, input_length = max_sequence_len-1))
model.add(Bidirectional(LSTM(100, return_sequences = False)))
model.add(Dense(total_words, activation = 'softmax'))
adam = Adam(lr=.01)
model.compile(loss='categorical_crossentropy', optimizer = adam, metrics = ['accuracy'])
history = model.fit(xs,ys,epochs=10, verbose=2)

seed_text = "country roads take me home to the place i belong"
next_words = 100
  
for _ in range(next_words):
	token_list = tokenizer.texts_to_sequences([seed_text])[0]
	token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
	predicted = model.predict_classes(token_list, verbose=0)
	output_word = ""
	for word, index in tokenizer.word_index.items():
		if index == predicted:
			output_word = word
			break
	seed_text += " " + output_word
print(seed_text)