num=11

if num>1:
    for i in range(2,num):
        if num%i==0:
            break
        
    else:
        print(f"number is prime:{num}")
            
else:
    print(f"number is not prime :{num}")            