def bracket_matching(input):
    #用栈进行括号匹配，并记录匹配失败的下标
    output=[' ' for _ in range(len(input))]
    i = 0
    bracket_stack = []
    while(i < len(input)):
        c = input[i]
        if (c != '(' and c != ')') :
            output[i] = ' '
        elif (c == '('):
            bracket_stack.append(i)
        elif (c == ')'):
           if len(bracket_stack) == 0:
               output[i] = '?'
           else:
               output[bracket_stack.pop()] = ' '
        i+=1
    while(len(bracket_stack)):
        output[bracket_stack.pop()] = 'x'
    output_str=''
    for c in output:
        output_str += c
    return output_str
# Examples
print("((IIII))))))")
print(bracket_matching("((IIII))))))"))
print("bge)))))))))")
print(bracket_matching("bge)))))))))"))
print("()()()()(uuu")
print(bracket_matching("()()()()(uuu"))
print("))))UUUU((()")
print(bracket_matching("))))UUUU((()"))