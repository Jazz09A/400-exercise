def calcularMaxMin(nums):
    min_value = nums[0]
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    
    print(f"El valor maximo es {max_value}")
    print(f"El valor minimo es {min_value}")

nums = [20,30,12,23,645,13,43]


#Parte 2
nums2 = []
for i in range(10):
    num = input(f"Ingresa numero {i+1}:")
    nums2.append(num)
calcularMaxMin(nums2)