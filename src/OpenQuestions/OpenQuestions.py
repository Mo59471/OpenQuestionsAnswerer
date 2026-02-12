import random

replay = True
while replay == True:
    with open("input.txt", "r") as file:
        lines = file.readlines()
        randInt = random.randint(0,len(lines)-1)
        question = lines[randInt]
    with open("output.txt", "a") as file:
        print("\n" + question)
        answer = input("\nInput an answer here: ")
        file.write("\n" + question + "\n" + answer + "\n")

    if input("\nAnswer recorded. Would you like to answer another question? Input 'y' to continue: ") != "y":
        replay = False
    
if input("\nWould you like to see your previous responses? Input 'y' to continue: ") == "y":
    with open("output.txt", "r") as file:
        print(file.read())
    
