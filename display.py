from colors import bcolors

def displaySign(src, first):
    floatValue = repr(src)
    if floatValue[0] != '+' and floatValue[0] != '-':
            floatValue = '+' + floatValue
    if (first and floatValue[0] == '+'):
        floatValue = floatValue[1:]
    else:
        floatValue = floatValue[0] + ' ' + floatValue[1:]
    return floatValue

def displayReduceForm(equation):
    first = 1
    strFinal = "Reduced form: "
    if equation[0] != 0:
        tmp = displaySign(equation[0], first)
        strFinal += tmp + " * X^2 "
        first = 0
    if equation[1] != 0:
        tmp = displaySign(equation[1], first)
        strFinal += tmp + " * X^1 "
        first = 0
    tmp = displaySign(equation[2], first)
    strFinal += tmp + " * X^0 = 0"
    print(bcolors.WARNING + strFinal + bcolors.END)