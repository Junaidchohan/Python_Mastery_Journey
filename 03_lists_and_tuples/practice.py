# Question_01 WAP to ask a user to enter name of their 3 fav movies & store them in a list

# name1 = input("Enter a name of your first movie : ")
# name2 = input("Enter a name of your second movie : ")
# name3 = input("Enter a name of your thired movie : ")

# movie = [name1, name2, name3]

# print(movie)


# Question_02 WAP to check if a list contains a palindrome of elements.
# palindrome ele is 121 aba 12321 abcba
ele1 = [1, 2, 3, 2, 1]
ele2 = [1, 3, 4, 2, 1]

newEle =  ele2.copy()
newEle.reverse()


if(ele2 == newEle):
    print("palindrome")
else:
    print("Not palindrome")
