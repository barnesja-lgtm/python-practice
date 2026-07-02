import keyboard

eRelease = True
while True:
    if keyboard.is_pressed("e") and eRelease:
        print("Yellow")
        eRelease = False

    elif not keyboard.is_pressed("e"):
        eRelease = True






