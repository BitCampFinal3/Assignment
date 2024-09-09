# 백준 9012번(스택 활용)

# 한 쌍의 괄호 기로오 된 "()" 문자열은 기본 VPS이라고 부른다.
# 입력값이 VPS면 YES를, 아니면 NO를 출력하시오.

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    vps_list = list(sys.stdin.readline().strip())
    stack_box=[]
    is_vps = True # vps가 유효한지 확인하는 변수

    for ele in vps_list:
        if ele == '(':
            stack_box.append(ele)
        elif ele == ')':
            if not stack_box:
                is_vps = False
                break
            else:
                stack_box.pop()

    # stack_box가 비어있고 is_vps가 true일 때
    if not stack_box and is_vps:
        print("YES")
    else:
        print("NO")


# 성능 요약
# 메모리: 31120KB
# 시간: 32ms