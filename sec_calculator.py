# Create a calculator that asks the user for a number (of days)
# and outputs how many seconds in that number of days

# Values - start by writing constants to hold:
# The number of seconds in a minute
SEC_MINS = 60
# The number of minutes in an hour
MINS_HOUR = 60
# The number of hours in a day
HOURS_DAY = 24

# Get input from the user and save it in a variable
Jeffery = input ("how many days do you want to convert into secounds")
# Change the value into an integer and resave in the variable
Jeffery = int(Jeffery)

# Calculate the number of seconds using * with the input and your constants. 

# Pual = Jeffery * HOURS_DAY * MINS_HOUR * SEC_MINS


# Save it in a new variable.

# Output the answer
number_hours = Jeffery * HOURS_DAY
number_hours = str(number_hours)
print (number_hours+" hours")

number_mins = Jeffery * HOURS_DAY * MINS_HOUR
number_mins = str(number_mins)
print (number_mins+" minutes")

number_secs = Jeffery * HOURS_DAY * MINS_HOUR * SEC_MINS
number_secs = str(number_secs)
print (number_mins+" secounds")
# ---------------------------------

# EXTENSION 1
# Also output how many total hours and how many total minutes in the days

# ---------------------------------
# EXTENSION 2
# Create another calculator that does the opposite (input is seconds, output is days)

# ---------------------------------

# EXPERT (for those who already know some Python)
# Create the calculator above, but...
#   allow your user to choose the input and output type (seconds, minutes, hours, days)
#   Loop the calculator so they can do it again with having to reopen the program.