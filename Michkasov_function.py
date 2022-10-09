def michkasov_function (number, base):
    result = 0
    while number % base == 0:
        number = number/base
        result = result + 1
    return result

array =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
array_result = []
for item in array:
    m = michkasov_function(item, 2)
    array_result.append(m)

print (array)
print (array_result)   
