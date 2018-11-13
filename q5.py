
for i in range (2,10000000000):
    count=0
    for j in range(1,20):
        if (i%j==0):
            count=count+1
            if(count==20):
                print(i)
    