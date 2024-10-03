from itertools import count

c1 = count(0, 8)
r1 = range(8,100, 2)

print(next(c1))
print(next(c1))

for i in c1:
    if i > 100:
        break
    print(i)

print()
print("Range")
for i in r1:
    print(i)
