print("Welcome to my computer quiz!")
playing=input("Do you want to play: ")

if playing.lower() !="yes":
    quit()

print("OKay! Let's play: \n")
score=0

answer=input("what does CPU stand for ? \n " )
if answer.lower() =="central processing unit":
    print("Correct! ")
    score +=1
else:
    print("You are wrong! its Incorrect answer")


answer=input("what does GPU stand for ? \n " )
if answer.lower() =="graphic processing unit":
    print("Correct! ")
    score +=1
else:
    print("You are wrong! its Incorrect answer")


answer=input("what does RAM stand for ? \n " )
if answer.lower() =="random access memory":
    print("Correct! ")
    score +=1
else:
    print("You are wrong! its Incorrect answer")


answer=input("what does PSU stand for ? \n " )
if answer.lower() =="power supply":
    print("Correct! ")
    score +=1
else:
    print("You are wrong! its Incorrect answer")


print("you got  " + str(score) +" question correct!")



























































