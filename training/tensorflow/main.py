import tensorflow as tf

class LSTM():
    def __init__(self, rnn_size, batch_size, learning_rate, training_seq_len, vocab_size):
        self.lstm_cell = tf.contrib.rnn.BasicLSTMCell(rnn_size)