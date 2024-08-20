import sys

n = sys.stdin.readline().rstrip()
n = int(n)
s = []
for i in range(n):
    s.append(sys.stdin.readline().rstrip())

s.sort()
s.sort(key=len)

result = []
for value in s:
    if value not in result:
        result.append(value)

for i in result:
    print(i)