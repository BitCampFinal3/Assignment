import sys

# Stack 클래스 정의
class Stack:
    def __init__(instance):
        # 스택 리스트 초기화
        instance.stack = []
    
    def push(instance, x):
        # 스택에 x 추가
        instance.stack.append(x)
    
    def pop(instance):
        # 스택에서 가장 위의 요소 제거 ➡️ 해당 값 반환
        # 빈 스택일 경우 -1 출력
        if instance.empty():
            return -1
        return instance.stack.pop()
    
    def top(instance):
        # 스택의 가장 위 요소 반환
        # 빈 스택일 경우 -1 출력
        if instance.empty():
            return -1
        return instance.stack[-1]
    
    def size(instance):
        # 스택의 현재 요소 개수 반환
        return len(instance.stack)
    
    def empty(instance):
        # 빈 스택일 경우 -1 / 빈 스택이 아닐 경우 0 반환
        return 1 if not instance.stack else 0

input = sys.stdin.read
data = input().splitlines()
# 명령어 개수 n 입력 받기
n = int(data[0])
# stack 클래스 인스턴스 생성
stack = Stack()
output = []  # 결과를 저장할 리스트입니다.

# n개 명령어 진행
for i in range(1, n + 1):
    command = data[i].split()
    if command[0] == "push":
        # "push" 명령어 ➡️ 스택에 값 추가
        stack.push(int(command[1]))
    elif command[0] == "pop":
        # "pop" 명령어 ➡️ 스택에서 값을 제거 후 결과에 추가
        output.append(stack.pop())
    elif command[0] == "top":
        # "top" 명령어 ➡️ 스택의 가장 위의 값 결과에 추가
        output.append(stack.top())
    elif command[0] == "size":
        # "size" 명령어 ➡️ 스택의 크기를 결과에 추가
        output.append(stack.size())
    elif command[0] == "empty":
        # "empty" 명령어 ➡️ 스택이 비어있는지 확인 후 결과에 추가
        output.append(stack.empty())

print("\n".join(map(str, output)))