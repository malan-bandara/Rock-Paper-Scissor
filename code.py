from random import choice

#generate a random 
def generateRandom():
    global random_element
    random_element = choice(possibilities)
    return random_element


#compare the element with the user input
def compare(random,ui):
    if ui == random:
        print("Yayyy! You got it right 🥳\n")
    elif count >= 3:
        print(f"You had {count} tries and you didn't make it!😭")
    else:
        print(f"Nah! You didn't got it this time. It was {random} 😞")
        userInput()


#take the user input
def userInput():
    global count
    user_input =input("\nEnter your guess: ").lower()
    if user_input in possibilities:
        count+=1
        compare(random_element,user_input)
    else:
        print("Enter a valid guess!🚫")
        userInput()

print("\033[1m\033[94mWELCOME TO ROCK-PAPER-SCISSOR")
count = 0
possibilities = ["rock","paper","scissor"]
generateRandom()
userInput()