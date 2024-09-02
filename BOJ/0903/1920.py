import sys

# 첫 번째 입력을 읽어 n에 저장 (정수 하나를 입력받음)
n = int(sys.stdin.readline().rstrip())

# 두 번째 입력을 읽어 리스트로 변환한 후 오름차순으로 정렬하여 arr1에 저장
arr1 = sorted(list(map(int, input().split())))

# 세 번째 입력을 읽어 m에 저장 (정수 하나를 입력받음)
m = int(sys.stdin.readline().rstrip())

# 네 번째 입력을 읽어 리스트로 변환하여 arr2에 저장
arr2 = list(map(int, input().split()))

# 이진 탐색 함수를 정의 (arr에서 target이 존재하는지 확인)
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    # start가 end보다 작거나 같을 때까지 반복
    while start <= end:
        mid = (start + end) // 2  # 중간 인덱스를 계산
        if arr[mid] == target:  # 중간 값이 target과 같으면
            return True  # True를 반환 (target이 arr에 존재)
        elif arr[mid] < target:  # 중간 값이 target보다 작으면
            start = mid + 1  # 탐색 범위를 오른쪽 절반으로 좁힘
        else:  # 중간 값이 target보다 크면
            end = mid - 1  # 탐색 범위를 왼쪽 절반으로 좁힘
    return False  # target이 arr에 존재하지 않으면 False를 반환

# arr2의 각 요소에 대해 이진 탐색 수행
for i in range(len(arr2)):
    result = binary_search(arr1, arr2[i])
    if result:  # 결과가 True이면
        print(1)  # 1을 출력 (arr1에 존재)
    else:  # 결과가 False이면
        print(0)  # 0을 출력 (arr1에 존재하지 않음)
