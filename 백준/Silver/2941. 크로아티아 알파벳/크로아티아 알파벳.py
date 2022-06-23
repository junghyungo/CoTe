cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]
w = input()
for i in cro: w = w.replace(i,"_")
print(len(w))