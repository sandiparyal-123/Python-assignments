import temperature 

while True:
    choice = int(input("1. Celsius to Farenheit \n2. Farenheit to Celsius \n3. Celsius to Kelvin \n4. Exit \n Select conversion:    "))

    if choice == 1:
        c = float(input("Enter Temperature:   "))
        temperature.cel_to_faren(c)

    if choice == 2:
        F = float(input("Enter Temperature:   "))
        temperature.faren_to_cel(F)

    if choice == 3:
        c = float(input("Enter Temperature:   "))
        temperature.cel_to_k(c)

    elif choice == 4:
        print ("Exiting program.")
        break
    else:
        print ("invalid, try again.")