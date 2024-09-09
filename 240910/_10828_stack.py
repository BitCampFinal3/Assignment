# 백준 10828번(stack활용)
# push X: 정수 X를 스택에 넣음
# pop: 맨 위 정수 뺀 다음, 그 수를 출력. 비어있으면 -1 출력
# size: 스택에 들어있는 요소 개수 출력
# empty: 스택이 비어있으면 1, 아니면 0 출력
# top: 스택의 가장 위에 있는 정수 출력. 비어있을 시엔 -1 출력

import sys

N = int(sys.stdin.readline())
stack_box = []

for _ in range(N):
    ele = sys.stdin.readline().strip()

    if "push" in ele:
        # 공백을 기준으로 자르고 마지막 요소 반환
        ele = ele.split()[-1]
        stack_box.append(ele)

    elif ele == "pop":
        # 만약 stack_box에 요소가 있다면
        if stack_box:
            res = stack_box.pop()
            print(res)
        else: # if not stack_box와 같은 의미
            print(-1)

    elif ele == "size":
        print(len(stack_box))

    elif ele == "empty":
        if not stack_box:
            print(1)
        else:
            print(0)

    elif ele == "top":
        if stack_box:
            print(stack_box[-1])
        else:
            print(-1)