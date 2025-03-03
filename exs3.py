def brackets(s):
    stack = []
    
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:

                return False

    return not stack

print(brackets("[12 / (9) + 2(5{15 * <2 - 3>}6)]"))
print(brackets("1{2 + [3}45 - 6] * (7 - 8) 9"))
