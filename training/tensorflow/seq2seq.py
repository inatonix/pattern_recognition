import tensorflow as tf
from tensorflow.nn.rnn_cell import LSTMCell
import numpy as np


def load_data(data_dir):
    return None

def get_embedding():
    return None

def train():
    return None

def predict():
    return None

class Seq2seq():
    def __init__(self, cell, batch_size, learning_rate):
        self.cell = cell
        self.batch_size = batch_size
        self.learning_rate = learning_rate

if __name__ == '__main__':
    ## initialize variables
    learning_rate = 0.1
    batch_size = 50
    vocab_size = 10000    
    num_units = 10

    # Embedding
    embedding_encoder = variable_scope.get_variable(
        "embedding_encoder", [src_vocab_size, embedding_size], ...)
    # Look up embedding:
    #   encoder_inputs: [max_time, batch_size]
    #   encoder_emb_inp: [max_time, batch_size, embedding_size]
    encoder_emb_inp = embedding_ops.embedding_lookup(
        embedding_encoder, encoder_inputs)

    encoder_cell = tf.nn.rnn_cell.LSTMCell(num_units)
    decoder_cell = tf.nn.rnn_cell.LSTMCell(num_units)

    encoder_outputs, encoder_state = tf.nn.dynamic_rnn(
        encoder_cell, encoder_emb, sequence_length=source_sequence_length, time_major=True)    
