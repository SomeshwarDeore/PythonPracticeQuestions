text=input("Enter any text :")
count=0

for i in text:
    if(i.isalpha()==True):
        count+=1
        
print(f"Total character in text is {count}")        