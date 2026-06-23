
"""print(5+5==10)
print(5+5==8)
print(5==5.0)
print('hello'=='hi')
print(5+5>=10)
print(5+5>=8)
print(5!=5)
print(5!=6)
print('hello'!= 'hi')
print(5=='5')"""

"""if 5 < 10 :
    print ("hello")
print ("good bye")"""

"""if 5<10:
    print ("less than ten")
else: 
    print ("ten or more")"""

"""print ('HELLO'.lower())

if 'HELLO'.lower() == 'hello' :
    print ("the same")"""

"""guess = input("whats the password?")
print("checking password is a match...")
while guess != 'secret' :
    guess = input('Try again')
    print("Checking password is a match...")
input("welcome")"""

"""user_input = input()
try:
    num = int(user_input)
    print (f'You picked {num}')
except:
    print(f'{user_input} is not a number') """

def calculate_area(x, y):
    print(f"Area : {x * y}")

calculate_area(2, 5)

def repeat_message(message, times):
    for i in range(times):
        print(message)

repeat_message("Hello", 5)

def check_play():
    play = input("Do you want to play again")
    if play.lower() in ["y", "yes"]:
        return True
    else:
        return False

check_play()

