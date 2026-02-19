import random

'''
1 for snack
-1 for water
0 for gun
'''

computer = random.choice([1, -1, 0])

youStr = input("Enter your choice (s/w/g): ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snack", -1: "Water", 0: "Gun"}

if youStr not in youDict:
    print("Invalid input!")
    exit()

you = youDict[youStr]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("Draw!")

elif computer == -1 and you == 1:
    print("You win!")

elif computer == -1 and you == 0:
    print("You lose!")

elif computer == 1 and you == -1:
    print("You lose!")

elif computer == 1 and you == 0:
    print("You win!")

elif computer == 0 and you == -1:
    print("You win!")

elif computer == 0 and you == 1:
    print("You lose!")