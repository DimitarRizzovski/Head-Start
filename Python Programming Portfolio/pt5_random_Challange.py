# Imports
import PySimpleGUI as sg
import random
# Random Number Generation
num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
# Difference Generation
actualdiff = abs(num1 - num2)
# Try statement incase something goes wrong
try:
    # Generates the layout
    layout = [[sg.Text('What is the difference between these two numbers?')],  # Title
              [sg.Text(num1), sg.Text(num2)],  # Adding in the numbers
              [sg.InputText()],  # Input text box
              [sg.Submit("Check Answer")]]  # Changes submit to check answer
    window = sg.Window("Random Number Game").Layout(layout)  # Generates the window with the name "Random Number Game"
    event, values = window.Read()  # Reads the values event is not used
    userdiff = int(values[0])  # Sets the users input in the text box to values
    window.Close() # Closes the window after the user put in the values
    if userdiff != actualdiff: # Checks if userdiff is not actualdiff
        sg.popup(f"Wrong! The diffrence between {num1} and {num2} is not {userdiff}", f"The difference is {actualdiff}") # If the user gets it wrong makes a popup
    elif userdiff == actualdiff: # Else if userdiff is equal to actualdiff
        sg.popup(f"Correct! The diffrence between {num1} and {num2} is {userdiff}") # Makes a popup menu that the user got it correct
except ValueError: # The most common error I get is a ValueError
    sg.popup("Please enter a valid number") # Pops up a menu telling the user to enter a valid number
