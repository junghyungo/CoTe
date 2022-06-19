t = int(input())
for i in range(t):
    s = input()
    for j in range(2,len(s)): 
        print(s[j]*int(s[0]), end="")
    print()