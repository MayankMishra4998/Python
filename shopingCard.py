food = []
prise = []
total = 0


while True:
    item = input("Enter a food to buy {q to quit} : ")
    if item == "q":
        break 
    else:
        food.append(item)
        item_prise = float(input(f"Enter the prise of {item} : ₹"))
        prise.append(item_prise)

total = sum(prise)
    
print("--------------Thing's you ordered---------------")  

for x in range(len(food)):
    print(f"You ordered : {food[x]} -> ₹{prise[x]}")  
    
print("--------------Total Bill---------------")        
print(f"Total Bill is  : {total} ₹")
      