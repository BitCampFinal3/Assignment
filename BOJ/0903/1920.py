import sys

n = int(sys.stdin.readline().rstrip())
arr1 = sorted(list(map(int, input().split())))

m = int(sys.stdin.readline().rstrip())
arr2 = list(map(int, input().split()))


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


for i in range(len(arr2)):
    result = binary_search(arr1, arr2[i])
    if result:
        print(1)
    else:
        print(0)