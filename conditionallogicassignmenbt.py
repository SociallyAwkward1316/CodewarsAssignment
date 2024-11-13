import random
randomnum = random.randrange(1, 10)
usernum = int(input("Please type a number 1-10"))

if randomnum == usernum:
    print("You guessed correctly!")
elif usernum > randomnum:
    print("Too High")
elif usernum < randomnum:
    print("Too low")