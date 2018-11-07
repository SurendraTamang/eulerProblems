a = 1
b = 2
i = 1
sum = b
while b<4000000:
    c = a + b

    a = b
    b = c
    if c%2 == 0:
        sum = sum +c
    i=i+1
print(sum)
# 4613732
