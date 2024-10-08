def calculator (firstNum, secondNum, operator):
    if (operator == 1):
        return firstNum + secondNum
    elif (operator == 2):
        return firstNum + secondNum
    elif (operator == 3):
        return firstNum * secondNum
    elif (operator == 4):
        return firstNum / secondNum
    elif (operator == 5):
        return firstNum % secondNum
    else: 
        return  0

exe = True

while (exe == True):
    print ("Escolha a operação: ")
    print ("1 - Soma (+) /n 2 - Subtração (-) /n 3 - Multiplicação (*) /n 4 - Divisão (/) /n 5 - Resto da divisão (%)")
    operator = int(input())
    if (operator <= 0) or (operator > 4):
        print ("Tente novamente")
    else: 
        print ("Insira o primeiro número do cálculo: ")
        firstNum = int(input())
        print ("Insira o segundo número do cálculo: ")
        secondNum = int(input())

        result = calculator(firstNum, secondNum, operator)
        print ("O reusltado da conta é: ", result)
