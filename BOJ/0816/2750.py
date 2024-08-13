import sys
N = int(sys.stdin.readline())
M = []
for i in range(N):
    M.append(int(sys.stdin.readline().rstrip()))

tmp = 0
for i in range(N):
    for j in range(1, N-i):
        if M[j-1] > M[j]:
            tmp = M[j-1]
            M[j-1] = M[j]
            M[j] = tmp

for i in range(N):
    print(M[i])