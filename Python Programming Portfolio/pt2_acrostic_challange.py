final_line = "" # Sets final_line to nothing or ""

for i in input("Input your topic word: ").upper(): # Starts a loop for the amount of characters that are inputted into the input, sets i to the currect selected letter and makes it all uppercase
    if i != " ": # Skippes all " " spaces in the users request e.g. H e l l o would be read as Hello
        while True: # Begins a loop
            try: # I put this here for exeptions that are generated whenever the users presses enter without adding any information
                line = input(f"{i}: ") # Prints i which is equal to the users current letter, then the user inputs a matching letter to what is asked, e.g. lets say i is equal to A then the user would see "A: "
                while line.strip()[0].upper() != i: # If the starting letter does not equal to the current value of i, e.g. the user inputs "A: b" the code will continue running and ask the user for the same letter
                    line = input(f"Please input the same letter {i}: ") # Clarifies to the user that they should have the same letter as the current value of i
                final_line += line.capitalize() + '\n' # Moves the users input to final_line and capitalizes the first letter e.g. "H: hello" turns into "Hello" when printed lastly adds in a new line so the characters can be on their own line
                break # Breaks out of the loop and the process starts again for all values of the users input
            except: # Except if theres an error
                print("Error: You entered an empty line or didn't add any information.") # The most common error is the user just pressing enter without adding in a character, if this occurs it just loops back
print(final_line) # Finally once all the letters of the input have been looped through it will print out final_line
