def print_field(pos):
    for line in pos:
        print(''.join(line))

def get_column(pos, i):
    return [x[i] for x in pos]

def is_win(pos, s):
    for line in pos:
        if ''.join(line) == len(pos) * s:
            return True
    for i in range(len(pos)):
        if ''.join(get_column(pos,i)) == len(pos) * s:
            return True

    flag = True
    for i in range(len(pos)):
        if pos[i][i] != s:
            flag = False

    if flag: return flag
    flag = True
    for i in range(len(pos)):
        if pos[i][-i-1] != s:
            flag = False
    if flag: return flag
    return False

def switch(s):
    if s == 'X':
        return 'O'
    return 'X'
        
def no_moves(pos):
    flat = [c for l in pos for c in l if c == '-']
    if len(flat) > 0:
        return False
    return True

def rate_pos(pos, s):
    if is_win(pos,s):
        #print(s,'is won')
        return 1 
    elif no_moves(pos):
        return 0
    return opt_move(pos, switch(s))

def opt_move(pos, s):
    max_rate = -1 
    for i in range(len(pos)):
        for j in range(len(pos)):
            if pos[i][j] == '-':
                pos[i][j] = s
                print_field(pos)
                input()
                r = -rate_pos(pos,s) 
                if r > max_rate:
                    max_rate = r 

                pos[i][j] = '-' 
                if max_rate == 1:
                    return max_rate
                
    return max_rate 

field = []
for i in range(2):
    field.append(['-','-'])
# print(field)

opt_move(field, 'X')
