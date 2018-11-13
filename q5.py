
for i in range(20, 10000000):
    count = 0
    for j in range(1, 21):
        if (i % j == 0):
            count = count+1
            if(count == 20):
                print(i)
