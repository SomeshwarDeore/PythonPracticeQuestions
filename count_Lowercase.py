String=input("Enter any String :")
count=0

for i in String:
    if ord(i)>=97 and ord(i)<=122:
        count+=1
        
print(f"Total number of lower case is :{count}")        