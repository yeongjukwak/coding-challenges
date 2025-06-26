t = int(input())
c = [int(input()) for _ in range(t)]

for i in c:
    rs = []

    for j in (25, 10, 5, 1):
        k, i = divmod(i, j)
        rs.append(str(k))

    print(' '.join(rs))
