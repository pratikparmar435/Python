import random

lst = ["insta","tiktok","sigma","isagi","rin","oliver","sae"]
random_word = random.choice(lst)
print("list of the word:",lst)
Guess_word = input("Guess the word:")
for i in range(10,0,-1):
    if Guess_word != random_word:
        Guess_word = input("wrong! guess again:")
        i -= 1
        print("Attempts left:",i)
print("Right guess, you win")

#or 
lst2 = ["reo","kunigami","ego","pratik","noa"]
word = random.choice(lst2)
guessedWord = ['_'] * len(word)
attempt = 4

