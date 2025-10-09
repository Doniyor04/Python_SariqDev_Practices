
from uzwords import words
import random as r

def get_word():
    word = r.choice(words)
    while "-" in word or " " in word:
        word = r.choice(words)
    return word.upper()

def display(let, word):
    display_letter = ""
    for letter in word:
        if letter in let:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    word_letters = set(word)
    user_letters = ''
    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")

        letter = input("Ҳарф киритинг: ").upper()
        if letter in user_letters:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} ҳарфи тўғри.")
        else:
            print("Бундай ҳарф йўқ.")
        user_letters += letter
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")
