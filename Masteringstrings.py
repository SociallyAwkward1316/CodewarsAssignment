mystring = "     Coding temple assignment!"

print(mystring.upper())
print(mystring.strip())
print(mystring.replace("Coding", "Banana"))
print(mystring.split())

import random
first = ["Christian", "Dylan", "Travis", "Katelyn"]
last = ["Sachs", "Katina", "Peck", "Mehner"]
print(f"Your name is " + random.choice(first) + " " + random.choice(last))