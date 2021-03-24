def bad_pos(pos):
       # print('bad_pos:',pos)
        if sum(pos) == 2:
            return True

        return not find_goodmove(pos)
            
def find_goodmove(pos):
        for r in range(3):
            for n in range(1,pos[r]+1):
                print('state:',pos,'current_move:',r,n)
                pos[r] -= n
                if bad_pos(pos):
                    print('->bad_pos',r,n)
                    pos[r] += n
                    return True
                pos[r] +=n 

        return False 

# initial state
pos=[3,4,0]
print(find_goodmove(pos))
