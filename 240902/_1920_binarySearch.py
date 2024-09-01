# 백준 1920번

# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))


n_list.sort()

# m_list안의 요소들을 돌아가면서 n_list에 들어있는지 이분탐색을 통해 확인
for i in m_list:
    left=0
    right=len(n_list) - 1

    while left <= right:
        mid = ( left + right ) // 2

        if n_list[mid] == i:
            print(1)
            break
        elif n_list[mid] > i:
            right = mid - 1
        else:
            left = mid + 1

    else:
        print(0)  







# 아래 코드는 설명 추가된 버전임용

# m_list안의 요소들을 돌아가면서 n_list에 들어있는지 이분탐색을 통해 확인
for i in m_list:

    # m_list를 순환할 때 마다 left,right값 초기화
    left=0
    right=len(n_list) - 1

    while left <= right:
        mid = (left+right)//2

        # 만약 중값값이 i와 같다면 1 출력
        if n_list[mid] == i:
            print(1)
            break

        #중간값이 i보다 크다면 right값을 중간좌표-1로 설정
        elif n_list[mid]>i:
            right = mid - 1

        #아니라면(중간값이 i보다 작다면) left값을 중간좌표+1로 설정
        else:
            left = mid + 1

    # while 루프가 break되지 않고 끝났을 때만(i값과 일치하는 값이 n_list에 없을 때) 0을 출력
    else:
        print(0)  




