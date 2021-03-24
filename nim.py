def bad_pos(pos):
       # print('bad_pos:',pos)
        if sum(pos) == 2:
            return True

        return not find_goodmove(pos)
            
def find_goodmove(pos):
        # print('find',pos,d)

        for r in range(2):
            for n in range(1,pos[r]+1):
         #       print(pos,n, pos[r])
                pos[r] -= n
                if bad_pos(pos):
                    print(r,n)
                    pos[r] += n
                    return True
                pos[r] +=n 

        
        return False 

# initial state
pos=[3,3]
find_goodmove(pos)
