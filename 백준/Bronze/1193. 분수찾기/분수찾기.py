x = int(input())
y = 1

while x>y:
    x -= y
    y += 1
    
if y%2==0:
    a = x
    b = y-x+1
else:
    a = y-x+1
    b = x

print(f"{a}/{b}")