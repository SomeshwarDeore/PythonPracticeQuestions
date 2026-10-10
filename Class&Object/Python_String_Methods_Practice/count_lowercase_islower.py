text=input("Enter any text :")
count=0

for i in text:
    if(i.islower()==True):
        count+=1

print(f"Total number of lower letter is :{count}")