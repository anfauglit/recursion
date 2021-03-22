def save_state(a):
	if len(a) == 0 or len(a) == 1:
		return True
	if len(a) == 2 and 'G' not in a:
		return True

def trans(A, B,out):
	if len(A) == 0:
		return True
	if save_state(B):
		for i in A:
			new_A = A[:]
			new_A.remove(i)
			B.append(i)
			if trans(B,A,out):
				out.append(i)
				return True

		if trans(B,A,out):
			out.append('F')
			return True
	out.pop()
	return False

out = []
A = list('GCW')
B = []
trans(A,B,out)
print(out)
