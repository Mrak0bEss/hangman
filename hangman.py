from hangmanforplayer import HangManForRusPlayer
from hangmanforplayer import HangManForEngPlayer
from printhang import PrintHang
from guess import HangmanGuessingEng
from guess import HangmanGuessingRus
from player import Player

N = Player()
while (N.lang != 'рус'  and N.lang != 'eng'):
    print('Неверный ввод языка(Lang error)')
    N.lang = input()
refresh = 'д' 
functoin=''
while (refresh == 'д' or refresh == 'y'):
    if (N.lang == 'рус'):
        print("Выбрана игра на русском")
        print('отгадать слово или загадать? введие о\з')
        function=input()
        if function == 'о':
            word = HangManForRusPlayer.rand_word()
            hide = HangManForRusPlayer.hide_word(word)
            HangManForRusPlayer.process_of_game(word,hide)
        elif function =='з':
            print('введите скрытые элементы с помощью _. Прмер ввода - c_о_о (слово).')
            hide=input()
            HangmanGuessingRus.Guess(hide)
        print('Хотите продолжить? (д/н)')
        refresh = input()
    elif (N.lang == 'eng'):
        print("Plying in english")
        print('guess a word or make a guess? enter o\m')
        function=input()
        if function == 'o':
            word = HangManForEngPlayer.rand_word()
            hide = HangManForEngPlayer.hide_word(word)
            HangManForEngPlayer.process_of_game(word,hide)
        elif function =='m':
            print('Enter the hidden elements using _. An example of input is w_rd (word).')
            hide=input()
            HangmanGuessingEng.Guess(hide)
        print('Want countinue? (y/n)')
        refresh = input()

    