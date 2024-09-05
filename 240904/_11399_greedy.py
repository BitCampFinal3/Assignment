# 백준 11399번(탐욕 알고리즘 활용)
# N명의 사람이 1대의 ATM기기에 줄 서있음
# i번 째 사람이 돈 인출하는 시간은 P분.


import sys

N = int(sys.stdin.readline())

time_list = list(map(int, sys.stdin.readline().split()))

# 인출 시간을 오름차순으로 정렬하는 것이 최적 해
time_list.sort()

time = 0
res_list = []

for p in time_list:
    
    # 각 사람이 돈을 인출하는데 필요한 시간
    time += p

    res_list.append(time)

res = sum(res_list)
print(res)
