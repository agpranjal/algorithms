string = input("Enter infix expression: ")
stack = []
output = ""
top = -1 
precedence ={
        "+" : 1, 
        "-" : 1,
        "*" : 2,
        "/" : 2
        }

for i in range(len(string)):
    if string[i] in "+-*/":
        if top == -1:
            stack.append(string[i])
            top += 1

        elif precedence[string[i]] > precedence[stack[top]]:
            stack.append(string[i])
            top += 1
        else:
            while True:
                if top == -1 or precedence[stack[top]] < precedence[string[i]]:
                    stack.append(string[i])
                    top += 1
                    break

                output += stack.pop()
                top -= 1

    else:
        output += string[i]

while top != -1:
    output += stack[top]
    top -= 1

print(output)
