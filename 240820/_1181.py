# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# 선택정렬 이용해서 문제풀기!!

# 선택정렬?
# 전체 데이터에서 가장 작은(또는 큰) 값을 찾아서 맨 앞에 배치하는 방식.

# 선택 정렬 과정 설명:
# 1. 리스트에서 가장 작은 값을 찾음
# 2. 그 값을 리스트의 맨 앞에 있는 값과 교환
# 3. 두 번째 위치부터 다시 이 과정을 반복. 즉, 두 번째 위치부터 리스트의 가장 작은 값을 찾아 두 번째 위치에 교환
# 4. 이 과정을 리스트의 끝까지 반복하면 리스트가 오름차순으로 정렬됨

import sys

# 개수 입력받기
n = int(sys.stdin.readline())

words=[]

# N개의 수를 배열로 입력받기
for _ in range(n):
    word = sys.stdin.readline().strip()
    words.append(word)


# 선택정렬을 이용하여 단어 정렬하는 함수
def selection_sort(words):
    
    # 배열의 길이만큼 반복
    for i in range(len(words)):
        
        # 현재 위치를 최소값으로 설정
        min_idx = i
        
        # 현재 위치 이후의 요소들을 비교
        for j in range(i+1, len(words)):
            
            # 조건 1: 단어의 길이를 비교
            # 더 작은 값이 있으면 그 위치를 최소값으로 설정
            if len(words[j]) < len(words[min_idx]):
                min_idx = j

            # 조건 2: 단어의 길이가 같으면 사전순(파이썬에서 문자열 간 비교는 사전순으로 비교 가능)
            elif len(words[j]) == len(words[min_idx]) and words[j] < words[min_idx]:
                min_idx = j
        
        # 찾은 최소값을 현재 위치와 교환
        words[i], words[min_idx] = words[min_idx],words[i]

# 단어 리스트 정렬 수행
selection_sort(words)

for word in words:
    print(word)



