# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 시간복잡도 고려해서 input() 대신에 sys.stidin.readline() 사용하기

import sys

# 개수 입력받기
n = int(sys.stdin.readline())

numbers=[]

# N개의 수를 배열로 입력받기
for num in numbers:
    int(sys.stidin.realine())
    numbers.append(num)
    
# 오름차순으로 정렬
numbers.sort()

print(numbers)




# 버블정렬 사용한 버전
import sys

n = int(sys.stdin.readline())

numbers=[]

for _ in range(n):
    num = int(sys.stdin.readline())
    numbers.append(num)
    
# 버블 정렬을 사용하여 정렬
for _ in range(len(numbers)):  # 리스트 길이만큼 반복
    for i in range(len(numbers) - 1):
        # 만약 i번째 요소 값이 다음 요소보다 크다면
        if numbers[i] > numbers[i + 1]:
            # 두 배열 요소의 자리 바꾸기
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
  
for num in numbers:
    print(num)