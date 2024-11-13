lst = []

addedlst = input("Book youd like to add to the list: ")

while True:
    addedlst = input("Type your book, type quit to stop: ")
    lst.append(addedlst)
    print("your book has been added!")
    
    if addedlst == "quit":
        lst.sort
        print(lst)
        break
