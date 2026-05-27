# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Get input
height = int( input("what is your height? ").replace("cm", ""))
age = int( input("what is your age? "))
vip = input("do you have a vip pass? ").upper().strip()
heart_problem = input("do you have a heart condition ")

# Check conditions and output verdict
if vip in ["TRUE", "YES"]:
    vip = True
    print("you are a vip, and are free to enjoy the ride")
else:
    vip = False
    if age < 11 and height < 151 and heart_problem == ["YES"]:
        print("your not suitable to go on this ride")
    else:
        print("you are allowed to go on this ride") 



# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient