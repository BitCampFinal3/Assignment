import sys

N = int(sys.stdin.readline().rstrip())
M = []
for i in range(N):
    M.append(sys.stdin.readline().rstrip())

M.sort()
M.sort(key=len)

result = []
for value in M:
    if value not in result:
        result.append(value)

for i in result:
    print(i)