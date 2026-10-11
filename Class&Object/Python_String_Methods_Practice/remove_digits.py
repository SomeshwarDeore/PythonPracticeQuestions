text=input("Enter any text :")

for i in text:
    if(i.isdigit()==True):
        text=text.replace(i,'')
        
print(text)        