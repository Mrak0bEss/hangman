#from distutils.command.config import LANG_ENG


from Levenshtein import distance
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import random
from tkinter import Y


class Player:
    name=''
    lang =''

class Print:

    def hang(i):
        if i == 1:
            print("""
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """)
        if i ==2:
            print("""
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """)
        if i == 3:
            print("""
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |     
    ----------
    """)
        if i == 4:
            print( """
     ------
     |    |
     |    O
     |   /|\\
     |    
     |   
     |   
    ----
    """)
        if i == 5:
            print( """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |   
     |   
    ----
    """)
        if i == 6:
            print( """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----
    """)
                        




#game
class HangManForRusPlayer:
   # выбор рандомного слова из файла
    def rand_word():
        with open('russian_nouns.txt', encoding='utf-8') as f:
            lines = f.read().splitlines()
        i=random.randint(0,len(lines))
        return lines[i]
    #генерация слова со спрятанными буквами
    def hide_word(s):
        if (len(s)>=7):
            count =5
        elif (len(s)>=5) :
            count=3
        else: count =2
        #hide_string='___'
        list1=[None]*len(s)
        list2=[None]*len(s)
        for i in range(len(s)):
          #  print(i)
            list2[i]=s[i]
            
        ban=set()   
        for i in range(len(s)):
            list1[i]='_'
        for i in range(count):
            while(True):
                j = random.randint(0,len(s)-1)
                if j not in ban:
                    ban.add(j)
                    break
            list1[j]=list2[j]
            hide_string=''.join(list1)
        return hide_string
    
    def process_of_game(word, hide_word):
        print("В и с е л и ц а")
        print(hide_word)
        count_of_error=0
        list1=[None]*len(word)
        list2=[None]*len(hide_word)
        while count_of_error<6:
            s=input()
            for i in range(len(word)):
          #  print(i)
                list1[i]=word[i]
                list2[i]=hide_word[i]
            if s in word:
                print('Такая буква есть!')
                for i in range(len(word)):
                        if list1[i] == s:
                            list2[i] = s
                hide_word=''.join(list2)
                print(hide_word)
            else:
                print('Ошибка!')
                count_of_error+=1
                Print.hang(count_of_error)
                hide_word=''.join(list2)
                print(hide_word)
            if list1 == list2:
                print('Игрок выйграл!')
                break
        if count_of_error == 6:
            print('Игрок проиграл')
            print('Слово - '+ word)
                
            
class HangManForEngPlayer(HangManForRusPlayer):
    def rand_word():
        with open('english_nouns.txt', encoding='utf-8') as f:
            lines = f.read().splitlines()
        i=random.randint(0,len(lines))
        return lines[i]        
    def process_of_game(word, hide_word):
        print("H a n g m a n")
        print(hide_word)
        count_of_error=0
        list1=[None]*len(word)
        list2=[None]*len(hide_word)
        while count_of_error<6:
            s=input()
            for i in range(len(word)):
          #  print(i)
                list1[i]=word[i]
                list2[i]=hide_word[i]
            if s in word:
                print('There is such a letter!')
                for i in range(len(word)):
                        if list1[i] == s:
                            list2[i] = s
                hide_word=''.join(list2)
                print(hide_word)
            else:
                print('Error!')
                count_of_error+=1
                Print.hang(count_of_error)
                hide_word=''.join(list2)
                print(hide_word)
            if list1 == list2:
                print('Player win!')
                break
        if count_of_error == 6:
            print('Player lose')
            print('Word - '+ word)  
  #ugadivanie
class Sravnenie:
    def chek(str1,str2):
        chk =False
        #print('----')
        for x in range(0,len(str1)):

            if (str1[x]!='_'):
                if(str1[x]==str2[x]):
                    chk=True
                else:
                   # print('----')
                    return False
        return chk        


#word=input()
#print(word)
#hide = HangManForRusPlayer.hide_word(word)
class HangmanGuessing:
    def Guess(hide1):    
        hide=[None]*len(hide1)
        for i in range(len(hide1)):
            #  print(i)
            hide[i]=hide1[i]
        #print(hide)     
        with open('russian_nouns.txt', encoding='utf-8') as f:
            lines = f.read().splitlines()
        setword=set()
        max=0
        min=0
        countOfErrors=0
        while (countOfErrors<6):
            for wrds in lines:
                if len(wrds)==len(hide) and Sravnenie.chek(hide,wrds):
                    if fuzz.ratio(hide,wrds)>max:
                        setword=set()
                        setword.add(wrds)
                        min=distance(wrds,hide)
                        max =fuzz.ratio(hide,wrds)
                    if fuzz.ratio(hide,wrds)==max:
                        setword.add(wrds)
            if len(setword)==1:
                print(setword.pop())
                break
            else:
               # print(setword)
                for x in setword:
                   # print(x)
                    while(True):
                        ind=random.randint(0,len(x)-1)
                        if hide[ind]=='_':
                            break
                    print('у вас есть ?')
                    print(x[ind])
                    answer=''
                    answer=input()
                    if (answer == 'д'):
                        hide[ind]=x[ind]
                        break
                    else:
                        countOfErrors=countOfErrors+1
                        Print.hang(countOfErrors)
                        if countOfErrors==6:
                            print('Бездушная машина не смогла отгадать слово')
                            break
               # print(hide)

        



N = Player()
print('Введите язык(Enter your lang (рус\eng)')
N.lang = input()
while (N.lang != 'рус'  and N.lang != 'eng'):
    print('Неверный ввод языка(Lang error)')
    N.lang = input()
refresh = 'д' 
functoin=''
while (refresh == 'д' or refresh == 'y'):
    if (N.lang == 'рус'):
        print("Игрок играет на языке " + N.lang)
        print('отгадать слово или загадать? введие о\з')
        function=input()
        if function == 'о':
            word = HangManForRusPlayer.rand_word()
            hide = HangManForRusPlayer.hide_word(word)
            count =0
            for  i in range(len(hide)):
                if hide[i]=='_':
                    count+=1  
            #print(len(hide)len(hide) - count)
            HangManForRusPlayer.process_of_game(word,hide)
        elif function =='з':
            print('введите скрытые элементы с помощью _. Прмер ввода - c_о_о (слово).')
            hide=input()
            HangmanGuessing.Guess(hide)
        print('Хотите продолжить? (д/н)')
        refresh = input()
    elif (N.lang == 'eng'):
        print("Player play in " + N.lang)
        word = HangManForEngPlayer.rand_word()
    #print(word)
        hide = HangManForEngPlayer.hide_word(word)
    #print(hide)
        HangManForEngPlayer.process_of_game(word,hide)
        print('Want countinue? (y/n)')
        refresh = input()

    