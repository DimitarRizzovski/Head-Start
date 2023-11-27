total = 0 # Sets total to 0

numbers_list = [] # Sets numbers_list to an empty list
while True: # Starts all the code in a loop
    try: # Tries the code indented
        for i in range(int(input("How many numbers would you like to have?: "))): # Asks the user how many numbers they wish to have, then proceeds to cycle i through each number in the list
            numbers_list.append(int(input(f"Number {i + 1}: "))) # Prints out Number and the current value of i + 1 so the user dosent see the list at point 0 they see it at point 1

        print("Your Numbers (Largest to Smallest)") # Tells the user that the program is printing out the numbers Largest to Smallest
        for i in sorted(numbers_list[int(input("Starting Position: ")) - 1:int(input("Finishing Position: "))], reverse=True): # Cycles i through the sorted number_list, and askes the user for the values of the list that they want to start and finish at, if the user enters a number above or below the list it just skipps, it also reverses the list to sort from highest to lowest
            print(i) # Prints the value of i at the current cycle

        for avg in numbers_list: # Cycles avg to be the total of numer_list's numbers
            total += avg # Sets the first number plus the second and third... to total

        len_numbers_list = len(numbers_list) # Sets the length of the numbers_list to len_numbers_list
        average = total / len_numbers_list # Divides the total by len_numbers_list to find the average or mean
        print(f"Average: {average}") # Tells the user what the average is
        break # Breaks out of the loop
    except: # If there is an exeption it will continue with the code below
        print("\n Sorry there has been an Error... Restarting \n") # Tells the user that theres been an error and restarts from the begginging
