t = int(input())

for i in range(t):
    s = input()
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
