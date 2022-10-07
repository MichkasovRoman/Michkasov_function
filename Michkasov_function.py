def Michkasov_function (number, base):
    result = 0
    while number % base == 0:
        number = number/base
        result = result + 1
    print (result)

Michkasov_function (375, 5)

array: int =[1,2,3]
index: int = 0
size: int = 3
element: int = array[0]
while index < size:
    m: int= Michkasov_function (array[index], 2)
    element = array[index]
    array[index] = array [m]
    array [m, 2] = element
    index = index + 1
print (array)
