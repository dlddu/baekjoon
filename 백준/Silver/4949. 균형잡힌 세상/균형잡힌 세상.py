pair = {")": "(", "]": "["}

while True:
    s = input()
    if s == ".":
        break
    stack = []
    answered = False
    for c in s:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")" or c == "]":
            if not stack or stack.pop() != pair[c]:
                print("no")
                answered = True
                break
    if not answered:
        if not stack:
            print("yes")
        else:
            print("no")
