def Michkasov_function (number, base):
    result = 0
    while number % base == 0:
        number = number/base
        result = result + 1
    print (result)

Michkasov_function (375, 5)
