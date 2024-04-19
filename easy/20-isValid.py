def isValid(s):
    sumbols = {
        '(': ')',
        '[':']',
        '{': '}'
    }
    stack = []
    for el in s:
        if el in sumbols:
            stack.append(el)
        elif stack and sumbols[stack[-1]] == el:
            stack.pop()
        else:
            return False
    return len(stack) == 0

print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(]")) # False