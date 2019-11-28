#!/usr/bin/env python3



def f(number):
    string_number = str(number)
    num = string_number.replace(',','')
    num = int(num)
    ans = 1
    for i in range(1,num+1):
        ans = ans*i

        
    nas = str(ans)
    print(nas)


    for i in range(len(nas)-1,-1,-1):
        
        if nas[i] =='0':
            count = 0
            res = ''
            for j in range(i-1,-1,-1):
               # print(f'--->{nas[j]}')
                if count >= 5:
                    print(res)
                    break
                if nas[j] == '0':
                    break
                else:
                    res = res + nas[j]
                   # print(f'--> rs{res}')

                    count = count + 1
        if len(res)==5:
            return res
    
                
    
if __name__ == "__main__":
    print("Main Started ")
    number = input("Enter the number function f(): ")
    res = f(number)
    ans = res[::-1]
    


    print(f'f({number})={ans}')
