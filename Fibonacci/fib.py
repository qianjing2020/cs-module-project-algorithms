# memoimized fibonacchi number fcn
def mem_fib(n, cache):
    # base case
    if (n == 0):
        cache[0] = 0
        return 0
    if (n == 1):
        cache[1] = 1
        return 1
    
    if n in cache:
        return cache[n]
        
    result_n_2 = mem_fib(n-2, cache)
    result_n_1 = mem_fib(n-1, cache)
    result_n = result_n_2 + result_n_1
    cache[n] = result_n
    
    return result_n

# # initialize cache out of function either list or dict
# cache = [0 for _ in range(n+1)]
# cache  = {i: 0 for i in range(n+1)}
import time
start_t = time.time()
print(f'Fibonacci 50 = {mem_fib(5, {})}')
print(f'Result calculated in {time.time()-start_t:.5f} seconds')
#print(cache)

# Tabulation example, start from 0 and go up to n
def tab_fib(n):
    # start at n = 0 and n = 1
    # initialize
    solution_table = [0 for _ in range(0, n+1)]
    solution_table[0] = 0
    solution_table[1] = 0
    
    for i in range(2, n+1):
        solution_table[i]= solution_table[i-1] + solution_table[i-2]
    
    print(solution_table)
    return solution_table[n]

start_t = time.time()
print(f'Fibonacci 50 = {tab_fib(50)}')
print(f'Result with tabulation algorithm with memoimization calculated in {time.time()-start_t:.5f} seconds')

# Use python built-in memoimization decorator
import functools
@functools.lru_cache()
def fib(n):
    # base case
    if (n == 0):
        return 0
    if (n == 1):
        return 1

    result_n_2 = fib(n-2)
    result_n_1 = fib(n-1)
    result_n = result_n_2 + result_n_1
    return result_n

start_t = time.time()
print(f'Fibonacci 50 = {fib(50)}')
print(f'Result with python memoimization calculated in {time.time()-start_t:.5f} seconds')

