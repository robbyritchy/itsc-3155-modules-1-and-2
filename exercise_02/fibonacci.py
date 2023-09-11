import time
import random




def fibonacci(n):
    a, b = 0, 1
    for i in range(2, n + 1):
            a, b = b, a + b
    return b

n = random.randint(15, 35)
result=fibonacci(n)


print(f"The {n}th term of the Fibonacci sequence is: {result}")

start_time = time.time()
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.6f} seconds")
