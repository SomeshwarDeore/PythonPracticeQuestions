Student={
    "name":"someshwar",
    "marks":{
        "phy":88,
        "math":77,
        "chem":90
    }    
}

Total=Student["marks"]["phy"]+Student["marks"]["math"]+Student["marks"]["chem"]
average=Total/3

if average>75:
    print("Excellent")
    
elif average>60:
    print("Good")    
    
elif average<60:
    print("Need improvement")    