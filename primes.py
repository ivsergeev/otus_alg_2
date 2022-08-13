from math import sqrt
from re import I

def alg1(n: int) -> int:
    '''1. Через перебор делителей.'''
    def is_prime(k):
        for j in range(2, k):
            if k % j == 0:
                return False
        return True
    primes = [i for i in range(2, n + 1) if is_prime(i)] 
    return len(primes)

def alg2_1(n: int) -> int:
    '''2. Несколько оптимизаций перебора делителей. Перебор до n/2'''
    def is_prime(k):
        for j in range(2, k // 2 + 1):
            if k % j == 0:
                return False
        return True
    primes = [i for i in range(2, n + 1) if is_prime(i)] 
    return len(primes)

def alg2_2(n: int) -> int:
    '''2. Несколько оптимизаций перебора делителей. Перебор до корень из n'''
    def is_prime(k):
        for j in range(2, int(sqrt(k)) + 1):
            if k % j == 0:
                return False
        return True
    primes = [i for i in range(2, n + 1) if is_prime(i)] 
    return len(primes)

def alg3(n: int) -> int:
    '''3. Решето Эратосфена со сложностью O(n log log n).'''
    mask = [1] * (n - 1)
    for p in range(2, n - 1):
        if mask[p - 2] == 1:
            k = 2 * p
            while k <= n:        
                mask[k - 2] = 0
                k += p
    return sum(mask)

def alg4(n: int) -> int:
    '''4. Решето Эратосфена с оптимизацией памяти: битовая матрица, по 32 значения в одном int'''
    mask = [0xffffffff] * ((n - 1) // 32 + 1)
    for p in range(2, n - 1):
        if mask[(p - 2) // 32] & 0x1 << (p - 2) % 32:
            k = 2 * p
            while k <= n:        
                mask[(k - 2) // 32] &= ~(0x1 << (k - 2) % 32) 
                k += p
    return sum(int(mask[i // 32] & 0x1 << i % 32 != 0) for i in range(n - 1))

def alg5(n: int) -> int:
    ''' 5. Решето Эратосфена со сложностью O(n)'''
    mask = [0] * (n - 1)
    primes = []
    for i in range(2, n + 1):
        if mask[i - 2] == 0:
            mask[i - 2] = int(i)
            primes.append(i)
        for p in primes:
            if p > mask[i - 2] or p * i > n:
                break
            mask[p * i - 2] = p
    return len(primes)
