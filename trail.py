
for i in range (11,10000):
    count=0
    for j in range(1,11):
        if (i%j==0):
            count=count+1
            if(count==10):
                print(i)
    