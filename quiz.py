firstanswer = ""
secoundanswer = ""
while firstanswer != 0:
    print("what is the most flamable gas?\nA: Hydrogen\nB: Nitrogen\nC: Neon")
    firstanswer = input("Answer: ").upper()
    if firstanswer == "A" :
        print("corect")
        firstanswer = 0
        while secoundanswer != 0:
            print("Sound is a mechanical wave that requires a physical medium to travel. which of these mediums does sound travel the fastest?\nA: Air\nB: Water\nC: stell")
            secoundanswer = input("Answer: ").upper()
            if secoundanswer == "C" :
                print("correct")
                secoundanswer = 0
            else:
                print("incorrect")
    else:
        print("incorrect")