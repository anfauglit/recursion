def was_good(pos):
	print('bad_pos:',pos)
	if sum(pos) == 0:
		return False 
	return not find_goodmove(pos)
		
def find_goodmove(pos):
	print('find',pos)

	for r in range(2):
		tmp = pos[r]
		print(tmp)
		for n in range(1,tmp+1):
			print(pos,n,id(n), id(tmp),tmp)
			pos[r] -= n
			if was_good(pos):
				return True 
			pos[r] += n
	return False 
				
# initial state
pos=[1,3]

find_goodmove(pos)
