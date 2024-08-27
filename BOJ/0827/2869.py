a, b, v = map(int, input().split())
count = 0
h = 0

if a >= v:
    count = 0
else:
    h = v - a
    count = int(h // (a - b))
    if h % (a - b) != 0:
        count += 1

print(count+1)
