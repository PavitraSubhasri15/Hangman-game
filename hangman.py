import nltk
from nltk.corpus import words
import random
nltk.download('words')
word_list=words.words()
word=random.choice(word_list)
word=word.lower()
print(word)
def hangman(word):
    
    word_len=len(word)
    curr_guessed_word=""
    for i in range(word_len):
        curr_guessed_word+="_ "
    print("CURRENT WORD:"+curr_guessed_word)
    curr_guessed_list = curr_guessed_word.rstrip().split(" ")
    lives=word_len+3
    guessed_letters=set()
    j=0
    Guessed=False
    while j<lives:
        letter=input("Guess the letter: ")
        before_add_guesstolist_len=len(guessed_letters)
        guessed_letters.add(letter)
        after_add_guesstolist_len=len(guessed_letters)
        if before_add_guesstolist_len==after_add_guesstolist_len:
            print("YOU HAVE ALREADY GUESSED THE LETTER {}. TRY TO GUESS OTHER LETTER".format(letter))
            continue
        print("Let's see if letter '{}' is in the word".format(letter))
        found=False
        for k in range(word_len):
            if letter==word[k]:
                found=True
                curr_guessed_list[k]=word[k]
        if found:
            print("YES, {} is in the word".format(letter))
        else:
            print("NO {} is not in the word".format(letter))
        j+=1
        curr_guessed_word=" ".join(curr_guessed_list)
        print("CURRENT WORD:"+curr_guessed_word)
        if '_' not in curr_guessed_word:
            Guessed=True
            break
        
        print("Lives left: {}".format(lives-j))
        print("__________________________________________________________________________")
    if(Guessed):
        print("HURRAY YOU HAVE GUESSED THE WORD")
    else:
        print("SORRY, YOU FAILED TO GUESS THE WORD")
        print("The actual word is {}".format(word))

hangman(word)
