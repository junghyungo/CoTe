natural = set(range(1, 10001))
generated = set()

for i in natural:
    for j in str(i): i += int(j)
    generated.add(i)

selfs = sorted(natural - generated)
for i in selfs: print(i)