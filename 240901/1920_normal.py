# (1) 자연수 N, N개의 정수 리스트 A, 자연수 M, M개의 정수 리스트 B 입력 받기
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# (2) B의 숫자들이 A에 존재하는지 확인
# e = element
for e in B:
    if e in A:
        print(1)
    else:
        print(0, "해당 값은 존재하지 않습니다.")