N, k = map(int, input().split())
x = list(map(int, input().split()))

for i in range(N):
    max_index = i
    for j in range(i + 1, N):
        if x[j] > x[max_index]:
            max_index = j
    # 현재 위치와 최대값 위치를 교환
    x[i], x[max_index] = x[max_index], x[i]

print(x[k-1])