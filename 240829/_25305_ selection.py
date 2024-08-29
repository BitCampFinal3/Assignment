import sys

n,k = map(int, sys.stdin.readline().split())
scores = list(map(int,sys.stdin.readline().split()))

# 선택정렬
for i in range(len(scores)):

    # 현재 위치를 최대값 인덱스로 설정
    max_idx = i         

    # i 다음번째부터 끝까지 순환
    for j in range(i+1, n):
        if scores[j] > scores[max_idx]:
            max_idx = j
            
    # 두 요소의 위치 교환
    scores[i],scores[max_idx] = scores[max_idx],scores[i]


# 커트라인 출력
print(scores[k-1])
