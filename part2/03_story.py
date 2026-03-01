#Part 1
#Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.
#Part 2
#Change the program so that the loop ends also if the user types in the same word twice in a row.
words = ""
wordf = ""
word = ""

while True:
    wordf = word
    word = input("Please type in a word: ")

    if word==wordf or word == "end":
        break
    
    words += word + " "


print(words)