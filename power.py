# -*- coding: utf-8 -*-

def alg1(x: float, n: int) -> float:
    '''1. Через обычные итерации.'''
    p = 1
    for i in range(n):
        p *= x
    return p

def alg2(x: float, n: int) -> float:
    ''' 2. Через степень двойки с домножением. '''
    p = 1 if n == 0 else x
    z = 1
    while z * 2 <= n:
        p *= p
        z *= 2
    for i in range(n - z):
        p *= x
    return p

def alg3(x: float, n: int) -> float:
    '''3. Через двоичное разложение показателя степени.'''
    p = 1
    d = x if n !=0 else 1
    while(n > 1):
        if n & 1 == 1:
            p *= d
        d *= d
        n >>= 1
    return p * d
