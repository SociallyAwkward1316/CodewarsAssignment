#Dictionaries        
friend_favs = {
'robert': ['cooking', 'gooey fries'],
'jimmy': ['shopping', 'basketball'],
'wilmer': ['ice skating', 'protien shake'],
}
for name, favthings in friend_favs.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for fav in favthings:  
        print("\t" + fav.title())
#Dictionary End

#User Input
age = input("How old is thou?")
age = int(age)

if age <= 13:
    print("You are but a child!")
elif age <= 18:
    print("You are but a teenager")
elif age  >= 19:
    print("You are an adult Jedi master")
#User Input end

#Function 1
def addition_sum(num1, num2):
    sum1 = int(num1) + int(num2)
    return sum1

numbers = addition_sum(input("Enter your a number: "), input("Enter a second one: "))
print(numbers)
#Function 1 End

#function 2
def addlist(num):
    
    sumlist = sum(numlist)  
    print(sumlist)
    return sumlist

numlist = [int(1), int(34), int(23), int(14)]
addlist(numlist)