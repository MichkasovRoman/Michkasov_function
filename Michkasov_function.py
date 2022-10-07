def Michkasov_function (number, base):
    result = 0
    while number % base == 0:
        number = number/base
        result = result + 1
    print (result)

Michkasov_function (375, 5)

array =[1,2,3]
index = 0
size = 3
element = array[0]
while index < size:
    index = Michkasov_function (array[index], 2)
    element = array[index]
    index = index +1
print (array)
