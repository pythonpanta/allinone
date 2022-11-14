import random
words=['nepal','cricket','umbralla','football']
word=random.choice(words)
chance=len(set(word))
guess_word='_'*len(word)

while chance !=0:
    print(guess_word)
    guess=input('Enter Guess...\n -> ').lower()
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guess_word=guess_word[:i]+guess+guess_word[i+1:]
        if guess_word==word:
            print('congratulation You won the Game')
            break
    else:
        chance-=1
        print('Wrong one... Try again')
        print(f'Remaining chance is {chance}')
        
else:
    print('You Loss The Match....')
    print(f'Correct Word is {word}')
print('Thank you')