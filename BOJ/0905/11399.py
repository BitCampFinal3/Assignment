import sys

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().split()))

P.sort()

total_time = 0
accumulated_time = 0

for time in P:
    accumulated_time += time
    total_time += accumulated_time

print(total_time)
