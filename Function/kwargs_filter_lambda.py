def function(**dict):
    marks=tuple(dict.values())
    return filter(lambda x:x>60,marks)
    
print(list(function(someshwar=100,sahil=88,krishna=55)))    