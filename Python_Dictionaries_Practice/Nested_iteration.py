Class={
    "Student":{
        "name":"someshwar",
        "age":18,
        "roll_no":40
    }
}

for key in Class.keys():
        for i,j in Class[key].items():
            print(f"{i}:{j}")