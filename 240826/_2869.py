# 2869번. 달팽이는 올라가고 싶당

# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 
# 또, 정상에 올라간 후에는 미끄러지지 않는다.

# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

import sys

# A, B, V 값 입력받기
a,b,v=map(int, sys.stdin.readline().split())

day = 1
res = a

while True:

    res = res + (- b + a) 

    day += 1

    if res >= v:
        break


print(day)




# 1트

# +a, -b 를 반복하는데 그 값이 V를 넘으면 중지
while True:
    # a미터를 올라간 뒤 v미터를 넘으면 중단
    res += a
    if res >= v:
        break

    # v미터를 넘지 않는다면 b미터를 내려간 뒤 day+1
    res -= b
    if res >= v:
        break

    day += 1


# 2트

day = 1
res = a

while True:

    res = res + (- b + a) 

    day += 1

    if res >= v:
        break









# A, B, V 값을 map을 사용하여 입력받은 이유?

# map()은 여러 문자열 값을 한 번에 내가 원하는 타입으로 변환하고, 
# 이를 각 변수에 쉽게 할당할 수 있기 때문. 
# map()을 사용하지 않으면 각 요소를 일일이 반복문으로 처리해야 함.
