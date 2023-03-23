from words import w
import itertools
from collections import Counter, defaultdict

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

counts = {}
cat = ''.join

def num_words(letter_list):
    possible_letters = [cat(c) for c in itertools.product(*letter_list)]
    return len(set(possible_letters).intersection(set(w)))

combs=['PHMTWDLFBS', 'EYHNRUOAIL', 'ENMLRTAOSK', 'DSNMPYLKTE']
word_count = num_words(combs)


ten_l = []
for (a,b,c,d,e,f,g,h,i,j) in itertools.combinations_with_replacement(letters, 10):
    ten_l.append(a+b+c+d+e+f+g+h+i+j)
print(len(ten_l))


high_cnt = word_count
high_combo = combs
for i in ten_l:
    for ii in ten_l:
        for iii in ten_l:
            for iiii in ten_l:
                comb = [i, ii, iii, iiii]
                cnt = num_words(comb)
                if curr_high < cnt:
                    high_cnt = cnt
                    high_combo =comb
                    print(high_cnt)
                    print(high_combo)





