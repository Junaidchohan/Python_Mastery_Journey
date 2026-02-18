print("Wellcome to the my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okey! Let's play :)")
score = 0

answer = input("what does CPU stand for? ")
if(answer.lower() == "centtral processing unit"):
    print("Correct answer!")
    score+= 1

else:
    print("Incorret!")

answer = input("what does GPU stand for? ")
if(answer.lower() == "graphics processing unit"):
    print("Correct answer!")
    score+= 1

else:
    print("Incorret!")



answer = input("what does RAM stand for? ")
if(answer.lower() == "Random access memory"):
    print("Correct answer!")
    score+= 1

else:
    print("Incorret!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + "%.")




