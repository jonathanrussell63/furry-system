import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #disables tf telling me i have wrong gpu
import tensorflow as tf
from tensorflow import keras


from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    'I love my dog',
    'I love my cat',
    'You love my dog!',
    'Do you think my dog is amazing?'
]

tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)
#padding makes all sentences the same size by adding 0's
#parameters: padding= put zeros before or after, maxlen = where to stop adding words, truncating = spot where words are cut off from 'post'
padded = pad_sequences(sequences,  padding = 'post') 
print("\nWord Index = " , word_index)
print("\nSequences = " , sequences)
print("\nPadded Sequences:")
print(padded)