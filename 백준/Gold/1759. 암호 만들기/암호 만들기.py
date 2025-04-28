import sys
input = sys.stdin.readline

l, c = map(int, input().split())
letters = input().split()
letters.sort()

#===========================
def make_pw(index, pw, moum, jaum):
    if (len(pw) == l) and (moum >= 1) and (jaum >= 2):
        print(''.join(pw))
        return

    for i in range(index, c):
        letter = letters[i]
        if (letter in ['a','e','i','o','u']):
            make_pw(i+1, pw+[letter], moum+1, jaum)
        else:
            make_pw(i+1, pw+[letter], moum, jaum+1)
    
#===========================

make_pw(0, [], 0, 0)