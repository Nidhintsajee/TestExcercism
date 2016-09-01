string=raw_input("Enter the brackets : ")
def check_brackets(string):
    counterparts = {')': '(', '}': '{', ']': '['}

    stack = []
    for char in string:
        if char in counterparts.values():
            stack.append(char)
        elif char in counterparts:
            if not stack:
                print False
            if stack.pop() != counterparts[char]:
                print False
    print not stack

check_brackets(string)
