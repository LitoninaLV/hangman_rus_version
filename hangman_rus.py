import random
from words_rus import word_list_rus
from words_rus import rus_alphabet

def get_valid_word(word_list_rus):
    word = random.choice(word_list_rus) #randomly chooses something from a list
    while len(word) > 9:  # only chooses words that are shorter than 9 characters to make the game simpler
        word = random.choice(word_list_rus)
    return word.upper()

def hangman():
    word = get_valid_word(word_list_rus)
    word_letters = set(word) # letters in the word
    alphabet = rus_alphabet
    used_letters = set() # what the user had guessed

    lives = 6
    
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f'У вас осталось {lives} жизней. Вы использовали следующие буквы: ', ' '.join(used_letters))
        
        # what the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Отгадайте слово: ', ' '.join(word_list))
        
        user_letter = input('Введите букву: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # takes away a life if player guessed wrong wrong
                print('Этой буквы нет в слове.')
        elif user_letter in used_letters:
            print('Вы уже использовали эту букву. Пожалуйста, попробуйте снова.')
        else:
            print('Недействующий знак. Попробуйте ещё раз')
    
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(f'Сожалеем, вы умерли. Загаданным было слово "{word}"')
    else:
        print(f'Вы отгадали слово "{word}", поздравляем!')

hangman()


