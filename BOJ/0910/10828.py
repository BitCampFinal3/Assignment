import sys
n = int(sys.stdin.readline().rstrip())
s = []
for i in range(n):
    o = sys.stdin.readline().split()
    if o[0] == 'push':
        s.append(o[1])
    elif o[0] == 'top':
        print(s[-1] if s else -1)
    elif o[0] == 'size':
        print(len(s))
    elif o[0] == 'empty':
        print(0 if s else 1)
    elif o[0] == 'pop':
        print(s.pop() if s else -1)
