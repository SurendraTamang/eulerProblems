a = 1
b = 2
sum = b
for i in range(1,4000000):
    c = a + b
    a = b
    b = c
    if i%2 == 0:
        sum = sum +c
print(sum)

