import time
def fib(n):
    if n <= 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    return result   

n = 40

start = time.time()
result = fib(n)
end = time.time()
elapsedTime = end - start

print("Wrong way took ", elapsedTime, " seconds")
print("Result for ", n, ": ", result)
