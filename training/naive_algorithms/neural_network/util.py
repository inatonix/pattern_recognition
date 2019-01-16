import numpy as np

def MSE(y,t):
    return np.sum(np.power(y-t,2)) * 0.5

def cross_entropy(y,t):
    delta = 1e-7
    return -np.sum(t * np.log(y+delta))

if __name__ == '__main__':
    print (cross_entropy(np.array([0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]), np.array([0,0,1,0,0,0,0,0,0,0])))
