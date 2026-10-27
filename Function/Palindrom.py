def Palindrom(Str):
    Str=Str.lower().replace(" ","")
    return Str==Str[::-1]

print(Palindrom("Someshwar"))