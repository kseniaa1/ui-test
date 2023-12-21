from math import tan

def ctg(x):
    return 1/tan(x)

def oper(x, y, op):
    if op == 1:
        return x+y
    elif op == 2:
        return x-y
    elif op == 3:
        return x*y
    elif op == 4:
        return x/y

def calculate(string):
    i = 0
    n = len(string)

    result = 0
    operation = 0
    ctg = 0
    while i < n:
        if string[i] >= '0' and string[i] <= '9':
            value = string[i]
            i += 1
            while i < n and string[i] >= '0' and string[i] <= '9':
                value += string[i]
                i += 1

            if operation > 0:
                if ctg == 1:
                    value = str(ctg(int(value)))
                    ctg = 0
                if (operation==4 and int(value)==0):
                    return "Error!"
                result = oper(result, int(value), operation)
                operation = 0

            else:
                if (result > 0):
                    return "Error!"
                if ctg == 1:
                    value = str(ctg(int(value)))
                    ctg = 0
                result = int(value)

        elif string[i] == '+':
            if operation > 0:
                return "Error!"
            operation = 1
            i += 1

        elif string[i] == '-':
            if operation > 0:
                return "Error!"
            operation = 2
            i += 1

        elif string[i] == '*':
            if operation > 0:
                return "Error!"
            operation = 3
            i += 1

        elif string[i] == '/':
            if operation > 0:
                return "Error!"
            operation = 4
            i += 1

        elif string[i] == 'c':
            if i < n - 2 and string[i+1]=='t' and string[i+2]=='g':
                ctg = 1
                i += 2
                return "Я не знаю ctg ("
            else: return "Error!"
        else: return "Error!"

    return str(result)


