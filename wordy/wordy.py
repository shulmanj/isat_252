import random
"""
    Wordle knock-off
    
    Jacob Shulman
    February, 2022
"""

def main():
    words = []
    with open('5letterwords.txt') as f: # read in words
        words = f.readlines()
    
    validGuesses = []
    with open('validGuesses.txt') as j: # read in valid guesses
        validGuesses = j.readlines()
    for i in range(len(validGuesses)): # remove new line from each word
        validGuesses[i] = validGuesses[i].strip()
    
    play = "y"
    while play == "y" or play == "yes":
        word = startGame(words)
        playGame(word, validGuesses)
        print("Play again? y/n: ", end = "")
        play = str(input())

    print("Goodbye")

# Gets the random word
def startGame(words):
    print("Welcome to Wordy. You have 6 tries to guess a random 5 letter word.")
    randomNumber = random.randrange(0, 5786)
    word = str(words[randomNumber].strip())
    return word


def playGame(word, vG):

    for i in range(6):
        guess = str(input())

        while len(guess) != 5 or guess not in vG:
            print("Please enter a valid 5 letter word:")
            guess = str(input())


        # dictionary to store colors of each letter, start as all black
        results = {i: "black" for i in range(5)}

        # counts the number of times each letter is in the guess
        count = {i: 0 for i in set(guess)} # convert to set to eliminate duplicates

        g = 0
        for i in guess: # check for greens
            count[i] += 1
            if i == word[g]:
                results[g] = "green"
            g += 1
        
        y = 0
        for i in guess: # check for yellows
            if i in word and word.count(i) >= count[i] and results[y] != "green":
                results[y] = "yellow"
            y += 1

        for i in range(5): # print the colors
            if results[i] == "green":
                print("🟩", end= "")
            elif results[i] == "yellow":
                print("🟨", end = "")
            else:
                print("⬛️", end = "")
        
        print()
        if guess == str(word):
            print("Good job! The word was", word)
            return
    if guess != word:
        print("Unlucky. The word was", word)



if __name__ == "__main__":
    main()
