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
		for index in range(i,len(s)):
			if s[index] not in s[i:index]:
				swapped = char_swap(s, i, index)
				print_perm(swapped, i+1)

def get_subset(s, res):
    if len(s) == 0:
        print(res) 
    else:
        get_subset(s[1:], res[:])
        res.append(s[0])
        get_subset(s[1:], res[:])

def get_tel_word(s, word, k):
    mapping = { 
            2: 'A',
            3: 'D',
            4: 'G',
            5: 'J',
            6: 'M',
            7: 'P',
            8: 'T',
            9: 'W',
        }
    if len(s) == 0:
        yield ''.join(word)
    else:
        for i in range(3):
            word[k] = (chr(ord(mapping[int(s[0])]) + i)) 
            yield from get_tel_word(s[1:], word[:], k+1)

tel = '6378687'
combinations = list(get_tel_word(tel, list(tel), 0))
