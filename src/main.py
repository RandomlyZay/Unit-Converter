import converters.area as area
import converters.currency as currency
import converters.data_storage as data_storage
import converters.distance as distance
import converters.energy as energy
import converters.power as power
import converters.pressure as pressure
import converters.speed as speed
import converters.temperature as temperature
import converters.time as time
import converters.volume as volume
import converters.weight as weight

def main():

    # Menu in alphabetical order
    print("Welcome to the Unit Converter!\n")

    print("1. Area")
    print("2. Currency")
    print("3. Data Storage")
    print("4. Distance")
    print("5. Energy")
    print("6. Power")
    print("7. Pressure")
    print("8. Speed")
    print("9. Temperature")
    print("10. Time")
    print("11. Volume")
    print("12. Weight")
    print("13. Exit")

    while True:
        try:
            userInput = int(input("\nWhat type of unit would you like to convert?: "))
            if userInput in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
                print("You have selected option", userInput)
                return userInput
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")
            
userInput = main()

if userInput == 1:
    pass
elif userInput == 2:
    pass
elif userInput == 3:
    pass
elif userInput == 4:
    pass
elif userInput == 5:
    pass
elif userInput == 6:
    pass
elif userInput == 7:
    pass
elif userInput == 8:
    pass
elif userInput == 9:
    pass
elif userInput == 10:
    pass
elif userInput == 11:
    pass
elif userInput == 12:
    pass
elif userInput == 13:
    print("Exiting the program.")
    exit()

if __name__ == "__main__":
    main()