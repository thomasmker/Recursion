def fib_non_optimized(n):
    if n == 0 or n == 1:
        return n
    
    return fib_non_optimized(n - 1) + fib_non_optimized(n - 2)

memoizedCache = {0:0, 1:1}
def fib_memoization(n):
    if n in memoizedCache:
        return memoizedCache[n]
    
    result = fib_memoization(n - 1) + fib_memoization(n - 2)
    memoizedCache[n] = result
    return result

num = 20
print(fib_non_optimized(num))
print(fib_memoization(num))