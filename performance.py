import time
import power
import primes
import fibo

def power_performance():
    algs = [power.alg1, power.alg2, power.alg3,]
    steps = [10, 10, 10,]
    for idx, alg in enumerate(algs):
        print(alg)
        for i in range(steps[idx]):            
            start = time.time()
            alg(2.0, 10**i)
            stop = time.time()
            print('n={} {} ms'.format(i, round((stop - start) * 10000) * 0.1))


def primes_performance():
    algs = [primes.alg1, primes.alg2_1, primes.alg2_2, primes.alg3, primes.alg4, primes.alg5,]
    steps = [6, 6, 6, 6, 6, 6,]
    for idx, alg in enumerate(algs):
        print(alg)
        for i in range(steps[idx]):            
            start = time.time()
            alg(10**i)
            stop = time.time()
            print('n={} {} ms'.format(i, round((stop - start) * 10000) * 0.1))


def fibo_performance():
    algs = [fibo.alg1, fibo.alg2, fibo.alg3, fibo.alg4,]
    steps = [2, 7, 3, 8,]
    for idx, alg in enumerate(algs):
        print(alg)
        for i in range(steps[idx]):            
            start = time.time()
            alg(10**i)
            stop = time.time()
            print('n={} {} ms'.format(i, round((stop - start) * 10000) * 0.1))


print('power')
power_performance()

print('primes')
primes_performance()

print('fibo')
fibo_performance()
