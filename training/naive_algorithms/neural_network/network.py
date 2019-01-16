import numpy as np

class MulLayer():
    def __init__(self):
        self.x = None
        self.y = None
    def forward(self,x,y):
        self.x = x
        self.y = y
        return x * y
    def backward(self,dout):
        return dout * self.y, dout * self.x

if __name__ == '__main__':
    apple = 100
    num = 2
    tax = 1.1

    mul1, mul2 = MulLayer(), MulLayer()
    
    apple_price = mul1.forward(apple,num)
    sum_price = mul2.forward(apple_price,tax)
    print("forward:",sum_price)

    d2 = mul2.backward(1)
    d1 = mul1.backward(d2[0])

    print("apple:",d1[0]," num:",d1[1]," tax:", d2[1])

