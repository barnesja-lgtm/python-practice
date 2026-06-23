firstanswer = ""
secoundanswer = ""
thirdanswer = ""
fourthanswer = ""
fifthanswer = ""
score = 10

while firstanswer != 0:
    print("what is the most flamable gas?\nA: Hydrogen\nB: Nitrogen\nC: Neon")
    firstanswer = input("Answer: ").upper().strip()
    if firstanswer == "A" or "HYDROGEN" :
        print("correct")
        firstanswer = 0
        while secoundanswer != 0:
            print("Sound: is a mechanical wave that requires a physical medium to travel. which of these mediums does sound travel the fastest?\nA: Air\nB: Water\nC: steel")
            secoundanswer = input("Answer: ").upper().strip()
            if secoundanswer == "C" or "STEEL" :
                print("correct")
                secoundanswer = 0
                while thirdanswer != 0:
                    print("third: what part of a shrimps body houses its brain?\nA: head\nB: stomach\nC: Throat")
                    thirdanswer = input("Answer: ").upper().strip()
                    if thirdanswer == "C" or "THROAT" :
                        print("correct")
                        thirdanswer = 0
                        while fourthanswer != 0 :
                            print("fourth: Astronomers calculated the average color of all the light in the universe. They call this beige/off-white hue:\nA: cosmic latte\nB: univeral swirl\nC: blue")
                            fourthanswer = input("Answer: ").upper().strip()
                            if fourthanswer == "A" or "COSMICLATTE" :
                                print("correct")
                                fourthanswer = 0
                                while fifthanswer != 0 :
                                    print("fifth: there are more trees than stars. Counterintuitively, there are an estimated 3 trillion trees on Earth, while there are only about _______ to ________ billion stars in the entirety of the Milky Way galaxy. what are the missing numbers?\nA: 50 to 75 \nB: 500 to 800 \nC: 100 to 400")
                                    fifthanswer = input("Answer: ").upper().strip()
                                    if fifthanswer == "C" or "100TO400":
                                        print("correct")
                                        fifthanswer = 0
                                        print(f"Finished your score was {score}/10")
                                        if score == 1 :
                                          print("you bearly passed")
                                        elif score == 10 :
                                            print("you got a perfect score, please touch grass")
                                        elif score <= 1 :
                                            print("you failed")
                                    else:
                                        print("incorrect")
                                        score -= 1
                            else:
                                print("incorrect")
                                score -= 1
                    else:
                        print("incorrect")
                        score -= 1
            else:
                print("incorrect")
                score -= 1
    else:
        print("incorrect")
        score -= 1