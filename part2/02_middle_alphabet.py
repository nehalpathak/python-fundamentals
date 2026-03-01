#Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.
#You may assume the letters will be either all uppercase, or all lowercase.

l1 = input("1st letter:")
l2 = input("2nd letter:")
l3 = input("3rd letter:")

if l1<l2<l3 or l3<l2<l1:
    print(f"The letter in the middle is {l2}")

elif l2<l1<l3 or l3<l1<l2:
    print(f"The letter in the middle is {l1}")

else:
    print(f"The letter in the middle is {l3}")