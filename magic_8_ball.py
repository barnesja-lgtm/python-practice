# =====================================================================
# PROJECT: The Magic 8-Ball Fortune Teller
# Create a program that gives random responses to yes/no questions
# =====================================================================

# TOOLS
# TODO: Import the 'random' module so we can pick a random index later.
import random

# RESPONSES
# TODO: Create a list called 'responses' that contains at least 8 different 
#       8-ball answers (strings). There should be positive answers, negative answers and neutral answers.
#       Examples: "Yes, definitely!", "Ask again later.", "Outlook not so good."
responses = ["maybe",'totaly',"definatly",'yup','i guess',"I'm not sure","seek help","in my profensional opion no","that's just a waste of time","your a horrible person for thinking that's a remotely good idea to ask that question","I dont know","just flip a coin"]
rare_respones = ["this convisationis boring ask again later","no.","your better off without that infomation"]
really_rare_respones = ["why.","just please stop asking questions","give up hope","ask again later"]
infinite = ''
# MAIN LOOP
# TODO Create an infinite loop
while infinite != 'quit' :
    

    # TODO: Ask the user to type in a Yes/No question about their future and save it in a variable.
    #       (Or tell them to type 'quit' to leave).
    print("Ask a yes or no question!")
    print("Or type 'quit' to leave ")
    Input = input().strip()
   
    # Check if the user wants to exit and break from the loop if they do.
    if Input == 'quit' :
        infinite = 'quit'
        continue
    # RANDOM REPSONSE
    # TODO: Step A: Calculate the last valid index of your list.
    #       (Remember: If a list has 5 items, the indexes are 0, 1, 2, 3, 4).
    #       Use random.randint() to get a number between 0 and that last index.
    #       Save it in a variable called 'random_index'.
    what_type_of_rarity = random.random()
    if what_type_of_rarity <= 0.7:
        print(random.choice(responses))
    elif what_type_of_rarity >= 0.8 and what_type_of_rarity <= 1:
        print(random.choice(rare_respones))
    elif what_type_of_rarity > 0.7 and what_type_of_rarity < 0.8 :
        print(random.choice(really_rare_respones))

    # TODO: Step B: Use your 'random_index' to grab the matching answer 
    #       out of your 'responses' list.
    #       Save it in a variable called 'chosen_fortune'.

    # TODO Print the result

# TODO Say goodbye to let them know the program has ended.

# ==================================================
# EXTENSION
# Common and rare responses
# TODO Split your responses into 2 lists. A common responses list and a rare responses list
# TODO Use random.random() or randint() to get a percentage
# TODO Check if the number is lower than 0.8 and use the common list to give a response if it is
# TODO Otherwise use the rare list

# ===================================================
# EXPERT
# Try creating a magic eight ball that gives random responses based on the question (eg. positive, negative, snarky, funny responses)
# TODO Create a dictionary (or multiple lists)
# TODO Check for key words in the question to decide what type of response. Eg. "will I" has positive responses, short questions have snarky responses, "think" has funny responses, etc.