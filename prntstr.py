def print_str(n):
	if n < 0:
		print('-',end='')
		print_str(-n)
	else:
		if n > 9: 
			print_str(int(n / 10))
		print(n % 10, end='')

def ithdigit(n, i):
	if i == 0:
		return n % 10
	return ithdigit(int(n/10), i-1)

def l_ithdigit(n, i):
	n_len = len(str(n))
	return ithdigit(n,n_len - i - 1)

def print_str_iter(n):
	for i in range(len(str(n))):
		print(l_ithdigit(n,i), end='')
		

n = 324234
neg_n = -453
print_str(n)
print()
print_str(neg_n)
print()
