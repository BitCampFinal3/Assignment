# FizzBuzz 문제는 
# i = 1, 2, ... 에 대해 다음 규칙에 따라 문자열을 한 줄에 하나씩 출력하는 문제입니다.

# i가 3의 배수이면서 5의 배수이면 “FizzBuzz”를 출력합니다.

# i가 3의 배수이지만 5의 배수가 아니면 “Fizz”를 출력합니다.

# i가 3의 배수가 아니지만 5의 배수이면 “Buzz”를 출력합니다.
 
# i가 3의 배수도 아니고 5의 배수도 아닌 경우 i를 그대로 출력합니다.

# FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 주어집니다. 
# 이때, 이 세 문자열 다음에 올 문자열은 무엇일까요?


import sys

arr = []

# 세 개의 값 입력해서 리스트에 저장
for _ in range(3):
    i = sys.stdin.readline()
    arr.append(i)

# 입력된 세 개의 값 분석
for i in range(3):
    if arr[i] == "FizzBuzz":
        arr[i] = 
    elif arr[i] == "Fizz":
        arr[i] = 
    elif arr[i] == "Buzz":
        arr[i] = 
    elif isinstance(arr[i],int) :
        arr[i] = int(arr[i])


# 조건에 맞는 그 다음 값 출력




if i % 3==0 || i % 5==0:
    a = “FizzBuzz”
elif i % 3==0 || i % 5!=0:
    a = “Fizz”
elif i % 3!=0 || i % 5!=0:
    a = i   




# isinstance(객체, 클래스_또는_클래스의_튜플)
# 파이썬에서 객체가 특정 클래스나 데이터 타입에 속하는지를 확인할 때 사용되는 내장 함수

# 예시
# x가 int 또는 float 타입인지 확인
# print(isinstance(x, (int, float)))  # True
