n = int(input())
p = str(input())
t = 0
r = 0

p = [int(m) for m in p.split(' ')]
p.sort()

for m in p:
    t += m
    r += t

print(r)
