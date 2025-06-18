items =[
    {"name":"carrot","price":10,"quantity":5},
    {"name":"brinjal","price":20,"quantity":16},
    {"name":"tomato","price":7,"quantity":5},
    {"name":"potato","price":3,"quantity":12},
]

#intilize total cost 
total_cost =0.0

#calculate cost 
for item in items:
    item_total =item["price"]*item["quantity"]
    total_cost+=item_total
    print(f"{item['quantity']} x {item['name']} @ ${item['price']:.2f} = ${item_total:.2f}")

          
print(f"\ntotalbill:${total_cost:.2f}")
