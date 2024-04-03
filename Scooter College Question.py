while True:
    player = input("Are you using (k)ilometers, or (m)iles?:")


    if player == "k":
        idk= float(input("How many kilometers would you like to scooter?"))
        idk2 = idk * 0.621371 #How we transform kilometers to miles
        print("That is", idk2, "miles")
        speed = 24.1402 #15 mph in kilometers
        time = idk / speed #How we find the time needed to go from point A to B given speed

        timeinminutes = time * 60 #How we find the time in minutes
        
        print("Total time in minutes:", timeinminutes)

        CompA = 1 + (0.15 * timeinminutes)
        CompB = 2.5 + (0.12 * (timeinminutes - 5))
        CompC = 5 + (0.06 * timeinminutes)

        if CompA < CompB and CompC:
            print("You should use Company A. It will cost $",CompA)

        if CompB < CompA and CompC:
            print("You should use Company B. It will cost $",CompB)

        if CompC < CompB and CompA:
            print("You should use Company C. It will cost $",CompC)




    elif player == "m":
        idk4= float(input("How many miles would you like to scooter?"))
        idk3 = idk4 * 1.60934
        print("That is", idk3, "kilometers")
        speed = 15
        time = idk4 / speed

        timeinminutes = time * 60

        print("Total time in minutes:", timeinminutes)

        CompA = 1 + (0.15 * timeinminutes)
        CompB = 2.5 + (0.12 * (timeinminutes - 5))
        CompC = 5 + (0.06 * timeinminutes)

        if CompA < CompB and CompC:
            print("You should use Company A. It will cost $",CompA)

        if CompB < CompA and CompC:
            print("You should use Company B. It will cost $",CompB)

        if CompC < CompB and CompA:
            print("You should use Company C. It will cost $",CompC)