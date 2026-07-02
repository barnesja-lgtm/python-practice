#set up
firstanswer = ""
secoundanswer = ""
thirdanswer = ""
fourthanswer = ""
fifthanswer = ""
score = 10
#the final score message displays when the players score = 0 or they finish the quiz
def finalscore():
    print(f"Finished your score was {score}/10")
    if score == 1 :
        print("you bearly passed")
    elif score == 10 :
        print("you got a perfect score, please touch grass")
    elif score <= 1 :
        print("you failed")

#the main quiz or as i like to call it rested while loop hell
while firstanswer != 0:
    #the first question
    print("what is the most flamable gas?\nA: Hydrogen\nB: Nitrogen\nC: Neon")
    firstanswer = input("Answer: ").upper().strip()
    if firstanswer in ["A", "HYDROGEN"] :
        print("correct")
        firstanswer = 0
        while secoundanswer != 0:
            #the secound question
            print("Sound: is a mechanical wave that requires a physical medium to travel. which of these mediums does sound travel the fastest?\nA: Air\nB: Water\nC: steel")
            secoundanswer = input("Answer: ").upper().strip()
            if secoundanswer in ["C", "STEEL"] :
                print("correct")
                secoundanswer = 0
                while thirdanswer != 0:
                    #the third question
                    print("third: what part of a shrimps body houses its brain?\nA: head\nB: stomach\nC: Throat")
                    thirdanswer = input("Answer: ").upper().strip()
                    if thirdanswer in ["C","THROAT"] :
                        print("correct")
                        thirdanswer = 0
                        while fourthanswer != 0 :
                            #the fourth question
                            print("fourth: Astronomers calculated the average color of all the light in the universe. They call this beige/off-white hue:\nA: cosmic latte\nB: universal swirl\nC: blue")
                            fourthanswer = input("Answer: ").upper().strip()
                            if fourthanswer in ["A","COSMICLATTE"] :
                                print("correct")
                                fourthanswer = 0
                                while fifthanswer != 0 :
                                    #the fifth question
                                    print("fifth: there are more trees than stars. Counterintuitively, there are an estimated 3 trillion trees on Earth, while there are only about _______ to ________ billion stars in the entirety of the Milky Way galaxy. what are the missing numbers?\nA: 50 to 75 \nB: 500 to 800 \nC: 100 to 400")
                                    fifthanswer = input("Answer: ").lower().strip()
                                    if fifthanswer in ["c","100to400","100400","!))TO$))","!))$))","100 to 400"]:
                                        print("correct")
                                        fifthanswer = 0
                                        finalscore()
                                        
                                    else:
                                        #this code activates when the player gets the question wrong
                                        print("incorrect")
                                        score -= 1
                                        if score ==0 : 
                                            finalscore()
                                            
                            else:
                                #this code activates when the player gets the question wrong
                                print("incorrect")
                                score -= 1
                                if score ==0 : 
                                    finalscore()
                                    
                    else:
                        #this code activates when the player gets the question wrong
                        print("incorrect")
                        score -= 1
                        if score ==0 : 
                            finalscore()
                            
            else:
                #this code activates when the player gets the question wrong
                print("incorrect")
                score -= 1
                if score ==0 : 
                    finalscore()

    else:
        #this code activates when the player gets the question wrong
        print("incorrect")
        score -= 1
        if score ==0 : 
            finalscore()


     