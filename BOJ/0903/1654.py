import sys

# 첫 번째 입력을 읽어 K와 N에 저장 (각각 K개의 랜선, N개의 필요한 랜선 길이)
K, N = map(int, sys.stdin.readline().split())

# K개의 랜선 길이를 입력받아 리스트 lan에 저장
lan = [int(sys.stdin.readline()) for _ in range(K)]

# 이진 탐색의 시작점과 끝점을 설정 (1부터 최대 랜선 길이까지)
start, end = 1, max(lan)

# 이진 탐색을 수행하여 랜선의 최대 길이를 찾음
while start <= end:
    mid = (start + end) // 2  # 중간값을 계산
    lines = 0  # 중간값으로 자른 랜선 개수를 셀 변수
    for l in lan:
        lines += l // mid  # 각 랜선을 중간값으로 나누어 몇 개의 랜선이 나오는지 계산
    if lines >= N:  # 필요한 랜선 개수보다 많이 나오면
        start = mid + 1  # 더 긴 길이를 시도하기 위해 시작점을 올림
    else:  # 필요한 랜선 개수보다 적게 나오면
        end = mid - 1  # 더 짧은 길이를 시도하기 위해 끝점을 내림

# 가장 긴 랜선 길이를 출력
print(end)
