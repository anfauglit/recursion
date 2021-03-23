def is_finished(state):
	l = len(state)
	mid = int(l/2)
	for i in range(mid):
		if state[i] != 'W':
			return False
	for i in range(mid+1,l):
		if state[i] != 'B':
			return False
	return True

def check_move(marble, pos, state):
	l = len(state)
	if state[marble] == 'B' and marble+pos < l:
		if state[marble+pos] == ' ':
			if pos == 1:
				return True
			if pos == 2 and state[marble+1] == 'W':
				return True
	if state[marble] == 'W' and marble-pos >= 0:
		if state[marble-pos] == ' ':
			if pos == 1:
				return True
			if pos == 2 and state[marble-1] == 'B':
				return True
	return False

def move_marble(marble, pos, state):
	if state[marble] == 'W':
		pos *= -1 
		
	tmp = state[marble+pos]
	state[marble+pos] = state[marble]
	state[marble] = tmp


def solve_Cindy(state):
	if is_finished(state):
		return True
	for i,m in enumerate(state):
		if check_move(i, 1, state):
			move_marble(i, 1, state)
			if solve_Cindy(state):
				print(f'{i}{m}+1')
				return True
			if m == 'B':
				move_marble(i+1, -1, state)
			else:
				move_marble(i-1, -1, state)
		if check_move(i, 2, state):
			move_marble(i, 2, state)
			if solve_Cindy(state):
				print(f'{i}{m}+2')
				return True
			if m == 'B':
				move_marble(i+2, -2, state)
			else:
				move_marble(i-2, -2, state)
	return False


a = list('BBBBBB WWWWWWW')
solve_Cindy(a)
