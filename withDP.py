import time
memo = {0: 0, 1: 1}
def fib(n):
    if n in memo:
        return memo[n]
    else:
        result = fib(n - 1) + fib(n - 2)
    memo[n] = result
    return result   

n = 50

start = time.time()
result = fib(n)
end = time.time()
elapsedTime = end - start

print("Right way took ", elapsedTime, " seconds")
print("Result for ", n, ": ", result)
