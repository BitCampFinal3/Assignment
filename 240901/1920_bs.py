# (1) 이분탐색문(Binary Search) bs 함수 정의
def bs(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False

# (2) 자연수 N, N개의 정수 리스트 A, 자연수 M, M개의 정수 리스트 B 입력 받기
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# (3) A 정렬
A.sort()

# (4) B의 숫자들이 A에 존재하는지 확인 - 이분탐색문(Binary Search) bs 함수 호출
# e = element
for e in B:
    if bs(A, e):
        print(1)
    else:
        print(0, "해당 값은 존재하지 않습니다.")