while True:
    s = input()
    if s == "0":
        break
    print("yes" if s == "".join(reversed(s)) else "no")
