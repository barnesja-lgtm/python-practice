### Secret Agent Login
# Create a login process for a secret agent

# Ask for the user's name and save it in a variable
Agent_name = input ("what is your name?")
# Ask for the password and save it in a variable
Password = input ("enter the password")
# Check if the password == 'Falcon'
if Password == "Falcon" :
    # Ouput that access has been granted and welcome user using their name
    print("Access has been granted, welcome " + Agent_name)
    # Ask for the user's age and save it in a variable
    Agent_age = input("whats your age?")
    # Change the age into an integer
    Agent_age = int(Agent_age)
    # If the user's age is under 13, tell them they are a spy in training
    if Agent_age <= 13 :
        print ("you are a spy in training")
    # If their age is under 18, tell them they are a junior spy
    if Agent_age <18 :
        print ("you are a junior spy")
    # If their age is 18 or over, tell them they are a Field Agent
    if Agent_age >= 18 :
        print ("you are a Field Agent")
# Output a goodbye
print ("goodbye")
# ___________________________

# EXTENSION

# Ask more questions to give your spy more information
# Look up how to use 'and' and 'or' to force more conditions (eg. they must be one of 3 users AND get the password correct)

# ___________________________

# EXPERT (For those who already know python)

# Create a SPY ID GENERATOR
# Your user must login using the correct password to access the generator
# Use a bunch of questions to generate an id. Eg. If their name has 4 or fewer letters, their ID is a random fruit plus other logic...