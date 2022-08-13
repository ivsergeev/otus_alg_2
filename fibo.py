# -*- coding: utf-8 -*-
from math import floor, sqrt

def alg1(n: int) -> int:
    '''1. Через рекурсию.'''
    if n < 2:
        return n
    return alg1(n - 1) + alg1(n - 2)

def alg2(n: int) -> int:
    '''2. Через итерацию.'''
    if n < 2:
        return n
    F = [ 0, 1]
    for i in range(n - 1):
        F[1] = F[0] + F[1]
        F[0] = F[1] - F[0]
    return F[1]

def alg3(n: int) -> int:
    '''3. Через формулу золотого сечения.'''
    phi = (sqrt(5.0) + 1.0) / 2.0
    return floor(phi**n/sqrt(5.0) + 0.5)

def alg4(n: int) -> int:
    '''4. Через возведение матрицы в степень.'''
    f = Matrix22.fibo
    fpown = f.pow(n)
    return fpown.x11

class Matrix22:
    def __init__(self, x11: float, x12: float, x21: float, x22: float):
        self.x11 = x11
        self.x12 = x12
        self.x21 = x21
        self.x22 = x22

    def pow(self, n: int):
        p = Matrix22.identity
        d = self
        while(n > 1):
            n //= 2
            d = d * d
            if n % 2 == 1:
                p *= d
        return p

    def __mul__(self, other):
        if other is None:
            raise ValueError
        if not isinstance(other, Matrix22):
            raise ValueError
        return Matrix22(self.x11* other.x11 + self.x12 * other.x21, 
                        self.x11* other.x12 + self.x12 * other.x22,
                        self.x21* other.x11 + self.x22 * other.x21,
                        self.x21* other.x12 + self.x22 * other.x22,)

    @classmethod
    def identity(cls):
        return Matrix22( 1.0 , 0,0, 0.0, 1.0)

    @classmethod
    def fibo(cls):
        return Matrix22( 1.0 , 1.0, 1.0, 0.0)
