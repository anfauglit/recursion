import numpy as np

def no_collision(x, y, field):
	N = len(field)
	for i in range(N):
		if field[x][i] == 1:
			return False
		
	for i in range(N):
		if field[i][y] == 1:
			return False

	for i in range(N):
		for j in range(N):
			if i+j == x+y and field[i][j] == 1:
				return False
			if i-j == x-y and field[i][j] == 1:
				return False
	return True
				
def put_queen(x, n, field):
	N = len(field)

	if n == 0:
		return True 

	for i in range(N):
		if no_collision(x, i, field):
			field[x][i] = 1
			if put_queen(x+1, n-1, field):
				return True
			else:
				field[x][i] = 0
	return False

n = 12 

field = np.zeros((n,n))
print(field)

if put_queen(0, len(field), field):
	print(field)
else:
	print('Failed to find a solution')


				
