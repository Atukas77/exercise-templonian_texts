def p(S):
    current = "\0"
    count = 0

    for char in S:
        if char == current:
            count += 1
        else:
            if count > 0:
                print(f"{count}{current}", end="")
            current = char
            count = 1

    if count > 0:
        print(f"{count}{current}")


def s(S):
    num = ""
    for char in S:
        if char.isdigit():
            num += char
        else:
            if num:
                print(char * int(num), end="")
                num = ""


def main():
    n, c = input().split()
    S = input()
    if c == "p":
        p(S)
    elif c == "s":
        s(S)

main()
