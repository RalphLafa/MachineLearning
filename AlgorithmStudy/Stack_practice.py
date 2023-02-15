def parentheses(input: str) -> bool:
    temp = []
    flag = 0
    for char in input:
        if char == ')':
            if temp.pop() != '(':
                flag += 1
        elif char == '}':
            if temp.pop() != '{':
                flag += 1
        elif char == ']':
            if temp.pop() != '[':
                flag += 1
        else:
            temp.append(char)
    if flag == 0:
        return True
    else:
        return False 