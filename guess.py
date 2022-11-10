from Levenshtein import distance
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import random

from printhang import PrintHang
from equal import Sravnenie


class HangmanGuessingRus:
    def Guess(hide1):    
        hide=[None]*len(hide1)
        for i in range(len(hide1)):
            #  print(i)
            hide[i]=hide1[i]
        #print(hide)     
        with open('singular_and_plural.txt', encoding='utf-8') as f:
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
            elif len(setword)==0:
                print("Такого слова нет в словаре(")
                break
            else:
               # print(setword)
                for x in setword:
                   # print(x)
                    while(True):
                        ind=random.randint(0,len(x)-1)
                        if hide[ind]=='_':
                            break
                    print('В слове есть такая буква? (напишите д/н)')
                    print(x[ind])
                    answer=''
                    answer=input()
                    if (answer == 'д'):
                        hide[ind]=x[ind]
                        break
                    else:
                        countOfErrors=countOfErrors+1
                        PrintHang.hang(countOfErrors)
                        if countOfErrors==6:
                            print('Бездушная машина не смогла отгадать слово')
                            break
               # print(hide)
class HangmanGuessingEng:
    def Guess(hide1):    
        hide=[None]*len(hide1)
        for i in range(len(hide1)):
            #  print(i)
            hide[i]=hide1[i]
        #print(hide)     
        with open('english_nouns.txt', encoding='utf-8') as f:
            lines = f.read().splitlines()
        setword=set()
        #print(1);
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
            elif len(setword)==0:
                print("There is no a such word in library(")
                break
            else:
               # print(setword)
                for x in setword:
                   # print(x)
                    while(True):
                        ind=random.randint(0,len(x)-1)
                        if hide[ind]=='_':
                            break
                    print('Is there such a letter in the word? (Enter y/n)')
                    print(x[ind])
                    answer=''
                    answer=input()
                    if (answer == 'y'):
                        hide[ind]=x[ind]
                        break
                    else:
                        countOfErrors=countOfErrors+1
                        PrintHang.hang(countOfErrors)
                        if countOfErrors==6:
                            print('The soulless machine could not guess the word')
                            break
