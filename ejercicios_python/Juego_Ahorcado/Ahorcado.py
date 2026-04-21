
import random

#Funcion que elija palabra aleatoriamente
def get_word(file_name):
    words= []
    with open(file_name, 'r') as file:
        for line in file:
            words.append(line.strip())

    length=len(words)
    index=random.randint(0,length - 1)
    return words[index]


#FUNCION QUE REGRESA GUIONES EN LUGAR DE LA PALABRA
def get_dashed_word(word, chars=""):
    dashed_word ='-' * len(word)
    for char in chars:
        new_word = ""
        for i in range(len(word)):
            if word[i] == char:
                new_word += char 
            else:
                new_word += dashed_word[i]
        dashed_word = new_word
    return dashed_word
#FUNCIO QUE PERMITE ELEGIR CATEGORIA DE PALABRA
def select_category():
    choices_menu= "Elige la categoria para jugar"
    choices_menu += "\n1. Comidas\n2. Animales\n3. Equipos:\n "
    choice = int(input(choices_menu))
    if choice == 1:
        word = get_word('comidas.txt')
    elif choice == 2:
        word = get_word('animales.txt')
    elif choice == 3:
        word = get_word("equipos.txt") 
    else:
        print('Opcion incorrecta')  
        return None 
    return word

    

def draw_hangman(errors):

    # VERSION COMPLETA (con dibujo)
    match(errors):
        case 1:
            hangman = '''
        |- - - - - - - 
        |
        |
        |
        |
        |
        |
        |
        |______________________________
        '''
        case 2:
            hangman = '''
        |- - - - - - - 
        |        |
        |
        |
        |
        |
        |
        |
        |______________________________
        '''
        case 3:
            hangman = '''
        |- - - - - - - 
        |        |
        |        O
        |
        |
        |
        |
        |
        |______________________________
        '''
        case 4:
            hangman = '''
        |- - - - - - - 
        |        |
        |        O
        |        |
        |        |
        |
        |
        |
        |______________________________
        '''
        case 5:
            hangman = '''
        |- - - - - - - 
        |        |
        |        O
        |       /|\\
        |        |
        |
        |
        |
        |______________________________
        '''
        case 6:
            hangman = '''
        |- - - - - - - 
        |        |
        |        O
        |       /|\\
        |        |
        |       / \\
        |
        |
        |______________________________
        '''
        case _:
            hangman = ""

    print(hangman)


def game():
    print('Bienvenido al juego del ahorcado')
    word =select_category()
    if word != None:
        print(get_dashed_word(word))

        chars = ''
        errors = 0
        while True:
            char = input('Ingresa una letra o una palabra completa: ')
            if (len(char) == 1 and char in word) or char == word:
                chars += char 
                dashed_word = get_dashed_word(word, chars)
                print(dashed_word)
                if (dashed_word == word):
                    print("GANASTE!")
                    break
                else:
                    errors += 1
                    draw_hangman(errors)
                    if errors == 6:
                        print("PERDISTE!")
                        print("La palabra era:", word)
                        break
            
    else:
        return
   
if __name__ == "__main__":
    game()