s1 = input()
s2 = input()
s3 = input()


def print_fb(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


if s1.isdigit():
    print_fb(int(s1) + 3)
elif s2.isdigit():
    print_fb(int(s2) + 2)
elif s3.isdigit():
    print_fb(int(s3) + 1)
