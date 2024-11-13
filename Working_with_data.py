# List Comprehensions
numbers = list(range(1,11))

squarednum = [value**2 for value in numbers]
print(squarednum)
# List Comprehensions end

# Conditional Logic
number = int (input ("Enter a Number to see if its even!!"))
if (number % 2) == 0:
    print ("The number is even")
    
else:
    print ("Number provided is not even")
# Conditional Logic End

#Pizza Topping 
toppinglist = []
userinput = input("Type your toppings, type exit to stop: ")

while userinput.lower() != 'exit':
    toppinglist.append(userinput)
    print("Adding " + toppinglist[-1])
    userinput = input("Enter another topping, type exit to stop ")
    
print("Heres your Toppings", toppinglist)