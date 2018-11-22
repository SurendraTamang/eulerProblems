num = 600851475143
i = 2
while i * i < num:
    print(i)
    while num % i == 0:
        num = num / i
        print(num)
    i = i + 1
print(num)
