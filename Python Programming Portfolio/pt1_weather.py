AskUser = input("Is it raining? ")

if AskUser != 'y':
    print("Have a nice day.")
else:
    AskUser = input("Is it windy aswell? ")
    if AskUser != 'y':
        print("Take an unbrella")
    else:
        print("It is too windy for an unbrella")
