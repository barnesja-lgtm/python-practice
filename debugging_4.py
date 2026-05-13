print("--- Daily Step Tracker ---")
steps = input("How many steps did you walk today? ")
steps = int(steps)
if steps >= 10000:
    print("Amazing! You walked over 10,000 steps! You are a Pro Athlete.")
if steps < 5000:
    print("Good start, but try to walk a bit more tomorrow!")
DAILY_GOAL = 5000
if steps == DAILY_GOAL:
    print ("Bullseye! You hit your goal exactly!")
if steps == 0 :
    print ("Did you forget your phone today? You have 0 steps!")
print ("Tracker closing...")