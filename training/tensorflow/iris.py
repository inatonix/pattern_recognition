import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
import tensorflow as tf


if __name__ == '__main__':
    sess = tf.Session()
    iris = datasets.load_iris()

    binary_target = np.array([1. if x == 0 else 0. for x in iris.target])
    


    x_data = tf.placeholder(shape=[None,1], dtype=tf.float32)

