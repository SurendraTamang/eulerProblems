# Euler Project question number three
result = 0
highest = 1 
for i in range(999, 1, -1):
    for j in range(999, 1, -1):
        product = i*j
        first_part=product
        mod = 0
        while product != 0:
            pro = product % 10
            mod = mod*10+pro
            product = int(product/10)
            second_part = mod
        if first_part == second_part:
            result = first_part
            if highest<result:
                highest=result
print(highest)        
        
        
