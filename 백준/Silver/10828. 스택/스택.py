from sys import stdin

N = int(input())

stack = []
for _ in range(N):
    s = stdin.readline().split()

    match s[0]:
        case "push":
            stack.append(s[1])
        case "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        case "size":
            print(len(stack))
        case "empty":
            if stack:
                print(0)
            else:
                print(1)
        case "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)
