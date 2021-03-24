from functools import lru_cache
import numpy as np
import itertools

def fact(n):
	if n == 1:
		return n
	return n * fact(n-1)

@lru_cache(maxsize=None)
def fib(n):
	if n == 1 or n == 2:
		return 1
	return fib(n-1) + fib(n-2)

def comp(a, b):
	if a <= b:
		return True 
	return False 

def power(a, n):
	if n == 0:
		return 1
	return a * power(a, n - 1)

def square(a):
	if a == 1:
		return 1
	return square(a-1) + 2*a-1

def gcd(x, y):
	if y == 0:
		return x
	return gcd(y, x % y)

def k_permutation(n, k):
	if k == 0:
		return 1 
	print(n,k, n-k+1)
	input()
	return (n-k+1) * k_permutation(n, k-1)
	
print(k_permutation(5, 3))
arr = np.random.randint(100, size=100)

index = len(arr) - 1 

not_sorted = arr.copy()

while (index > 0):
	for i in range(index):
		if comp(arr[i], arr[i + 1]):
			tmp = arr[i]
			arr[i]  = arr[i+1]
			arr[i+1] = tmp
	index -= 1


