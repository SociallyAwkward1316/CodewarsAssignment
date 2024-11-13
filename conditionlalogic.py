weather = input("Type whether it is raining or sunny: ")
mood = input("type whether your happy or tired: ")

if "sunny" in weather:
    print("Stay indoors you bum")
elif "raining" in weather:
    print("Go for a hike")
    
if "happy" in mood:
    print("Go have fun")
elif "tired" in mood:
    print("Go to bed")