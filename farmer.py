import numpy as np

def next_move(c):
    while True:
        yield c[0]
        c = c[1:] + c[:1]

def finished(s):
    return 0 not in s.values()

def save_state(s, departure):
    a = [i for i,v in s.items() if v == departure]
    if len(a) == 0 or len(a) == 1:
        return True
    if len(a) == 2 and 'G' not in a:
        return True

    return False

def trans(state, moves, departure, out):
    departure ^= 1

    if finished(state):
        return True

    for i in range(4): 
        move = next(moves)
        if move == 'F':
            if save_state(state, departure):
                out.append(move)
                if trans(state, moves, departure, out):
                    return True
                out.pop()
        elif state[move] == departure:
            state[move] ^= 1
            if save_state(state, departure):
                out.append(move)
                if trans(state, moves, departure, out):
                    return True
                out.pop()
            state[move] ^= 1

    return False

out = []
a = list('CGW')
b = list(np.zeros(3, int))
state = dict(zip(a,b))
gen = next_move('CGWF')
trans(state, gen, 1, out)
print(out)
