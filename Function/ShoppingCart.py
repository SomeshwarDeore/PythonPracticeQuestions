def total_Spend(cart):
    total_cost=0
    for item in cart:
        total_cost+=item["Price"]*item["Quantity"]
        
    return total_cost    

cart=[
    {"name":"Appple","Price":100,"Quantity":3},
    {"name":"Banana","Price":20,"Quantity":12}
]

print(total_Spend(cart))