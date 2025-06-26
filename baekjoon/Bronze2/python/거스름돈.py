amount = int(input())
result = 0

change = 1000 - amount

cnt, change = divmod(change, 500)
result += cnt

cnt, change = divmod(change, 100)
result += cnt

cnt, change = divmod(change, 50)
result += cnt

cnt, change = divmod(change, 10)
result += cnt

cnt, change = divmod(change, 5)
result += cnt

cnt, change = divmod(change, 1)
result += cnt

print(result)
