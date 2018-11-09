number = 600851475143
list=[]
for i in range(2,number):
    count=0
    if number%i==0:
        for j in range(2,i):
            if i%j==0:
                count=count+1
        if count==0:
            print(i)
