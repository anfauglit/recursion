def char_swap(s, n, m):
	new_s = list(s) 
	tmp = new_s[n]
	new_s[n] = new_s[m]
	new_s[m] = tmp
	return ''.join(new_s)

def print_perm(s, i):
	if i == len(s)-1:
		print(s)
	else:
		print_perm(s[:], i+1)
		for index in range(i+1,len(s)):
			if s[index] not in s[i:index]:
				swapped = char_swap(s, i, index)
				print_perm(swapped, i+1)

mystring = 'ABBD' 
print_perm(mystring, 0)
