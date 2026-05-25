""" User input related functions"""

def getuserint(prompt):
    """colletcs user input as int or returns error"""
    while True:
        userinput = input(prompt)
        if userinput == 'q':
            return None
        else:
            try:
                return int(userinput)
            except ValueError:
                print("Please enter number, not text. Make your input again.")