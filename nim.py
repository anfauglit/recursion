def lts(a):
    return ''.join(list(map(str,a)))

def bad_pos(pos):
	global call_number
	call_number += 1
   # print('bad_pos:',pos)
	if sum(pos) == 2:
		return True

	return not find_goodmove(pos)
            
def find_goodmove(pos):
    global pos_stack
    
    init_pos = pos[:]
    for r in range(len(pos)):
        for n in range(1,pos[r]+1):
            print('state:',pos,'current_move:',r,n, 'stack:',pos_stack)
            pos[r] -= n
            if lts(pos) in pos_stack.keys() and pos_stack[lts(pos)] == 'u':
                pos[r] +=n 
                continue 
            elif lts(pos) in pos_stack.keys() and pos_stack[lts(pos)] == 'b':
                print('->bad_pos',r,n)
                pos[r] += n
                return True
            elif bad_pos(pos):
                pos_stack[lts(pos)] = 'b'
                print('->bad_pos',r,n)
                pos[r] += n
                pos_stack[lts(init_pos)] = 'g'
                return True
            pos[r] +=n 
            pos_stack[lts(pos)] = 'u'

    return False 

# initial state
call_number = 0
pos=[3,4,5]
pos_stack = {}

print(find_goodmove(pos))
print(call_number)
