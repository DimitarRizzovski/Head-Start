Scoreboard = {} # Sets scoreboard to a dicsinarry
round_number = 1 # Sets the round number
def LoopKeys(): # Defines Loop Keys
    print("** Scoreboard **") # Prints out ** Scoreboard ** every time LoopKeys is called
    for key, value in Scoreboard.items(): # Loops through all the keys and values in Scoreboard
        print(f"{key} - {value}") # Prints out the key then a - then the value of the key
while True: # While true allows it to loop so the user can ask the program as many times as they want
    try: # If there is an error the try and except function will catch it and revert it back to this stage
        Winner = input(f"Enter the winner for round {round_number}: ") # Users input for the winner
        if Winner == "X": # If the user types in X then
            print("** GAMEOVER **") # Prints ** GAMEOVER ** 
            LoopKeys() # Runs the LoopKeys Funtion
            break # Breaks out of the loop
        elif Winner in Scoreboard: # If the Winner is in Scoreboard then
            Scoreboard[Winner] += 1 # Increase its value by 1
            LoopKeys() # Runs the LoopKeys Function
        else: # If the user does not type in X or a currently added team then
            Scoreboard[Winner] = 1 # Add the new team at the value of 1
            LoopKeys() # Runs the LoopKeys Function
        round_number += 1 # Finally adds 1 to the round number this only runs after the user puts in a team and after everything else is ran
    except: # Except if there is an error
        print("Sorry there has been an unknown error, resetting...") # Tells the user that there is an unknown error and resets the program to the start
