import random

def print_str(n):
	# decompose the integer n and prints its digits one by one
	if n < 0:
		print('-',end='')
		print_str(-n)
	else:
		if n > 9: 
			print_str(int(n / 10))
		print(n % 10, end='')

def digitsum(n):
	# calculate the sum of all its digits
	if n < 0:
		return digitsum(-n)
	else:
		if n > 0: 
			return digitsum(int(n / 10)) + (n % 10)
		return 0

def digital_root(n):
	# digital root of an integer calculated recursivly as the sum of 
	# all its digits and stops when the sum becomes a signle digit integer
	print(n)
	if int(n / 10) == 0:
		return n
	return digital_root(digitsum(n))

def ithdigit(n, i):
	# returns digit at the i'th position in the integer n
	# positions are counted from the right
	if i == 0:
		return n % 10
	return ithdigit(int(n/10), i-1)

def l_ithdigit(n, i):
	# returns digit at the i'th position in the integer n
	# positions are counted from the left 
	n_len = len(str(n))
	return ithdigit(n,n_len - i - 1)

def print_str_iter(n):
	for i in range(len(str(n))):
		print(l_ithdigit(n,i), end='')
		
def print_str_1(n):
	# print empty string if n equals zero
	if n > 0:
		print_str_1(int(n / 10))
		print(n % 10, end='')
	
def print_tab(n):
	print(n * '    ', end='')

def do_nothing(d):
	return	

def simple_statement(d):
	print_tab(d)
	print('this is a python statement')

def if_statement(d):
	print_tab(d)
	print('if (condition):')
	make_block(d+1)

def for_statement(d):
	print_tab(d)
	print('for x in y:')
	make_block(d+1)

def make_statement(d):
	n = random.randint(0,2)	
	opts = [simple_statement, if_statement, for_statement]
	opts[n](d)
	
def make_block(d):
	# generating random syntactically correct python-like programs
	if d > 10:
		simple_statement(d)
	else:
		n = random.randint(0,1)	
		make_statement(d)
		opts = [do_nothing, make_block]
		opts[n](d)

make_block(0)
