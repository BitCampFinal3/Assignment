# bisect라이브러리?
# bisect(리스트, 항목) 함수는 항목을 리스트에 넣었을 때 삽입되는 인덱스를 반환

import sys
import bisect

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

n_list.sort()

for m in m_list:
  
  # n_list에서 m이 들어갈 자리의 바로 왼쪽에 있는 값이 m과 같은 값인지 확인
  if n_list[bisect.bisect(n_list, m) - 1] == m :
    print(1) # 같으면 리스트 내에 해당 숫자가 있는 것이므로 1 반환
  else:
    print(0)


# 메모리: 49296KB
# 시간: 260	ms

# 이분탐색 알고리즘을 이용하는 것과 메모리를 비슷하나 시간은 반 이상 절감!
