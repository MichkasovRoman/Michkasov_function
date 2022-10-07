def Michkasov_function (number, base):
    result = 0
    while number % base == 0:
        number = number/base
        result = result + 1
    print (result)

array =[1,2,3]
index = 0
size = 3
element = array[0]
while index < size:
    m = Michkasov_function (array[index], 2)
    array[index] = m
    index = index + 1
print (array)
