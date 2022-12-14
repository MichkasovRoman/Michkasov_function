def michkasov_function (number, base):
    result = 0
    while number % base == 0:
        number = number/base
        result = result + 1
    return result

array =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
array_result = []
for item in array:
    m = michkasov_function(item, 2)
    array_result.append(m)

print ("Set of integer function arguments X = ", array)
print ("Set of function values Y =", array_result)   

from matplotlib import pyplot as plt   
#ploting our canvas   
plt.plot(array,array_result)   
#display the graph# 
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Plot of the Michkasov function with base n = 2")    
plt.show()   
