# 3 Question Quiz - Debug all the errors, including any semantic errors.

print("Hello!")
print("This is a quick 3 part quiz. A question will be asked, and then you answer it")


print("First question:")
first_answer = input("How many millimetres in a centimetre?")
if first_answer != ("10") :
    print("incorrect the answer is 10")

if first_answer in ("10") :
    print("correct the answer is 10!")

print("Next Question:")
secound_answer = input("What is the capital of New Zealand?")
if secound_answer != ("Wellington, wellington") :
    print("incorrect the answer is Wellington")

if secound_answer in ("Wellington, wellington") :
    print("The answer is Wellington. That was easy, wasn't it?")


print("Final Question!")
last_question = input("What is 3 x 6?")
if last_question != ("18") :
    print("The answer is 18 silly!")

if last_question in ("18") :
    print("correct the answer is 18")