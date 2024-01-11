import sys

import random
from data import *
def next_time():
    print('Хотите сыграть ещё раз?')
    print('1. Да\n'
          '2. Нет')
    answer = input('Ваш выбор:')
    if answer == '1':
        return 1
    if answer == '2':
        return 0



def game(lives, word_list, record):
    record = record
    word_list = word_list

    if word_list == []:
        print("Вы отгадали все слова! Поздравляю!")
        get_record(record)


    else:
        word = word_list.pop(random.randrange(len(word_list)))
        count_lives = int(lives)
        word_hunt = '*' * len(word)


        while True:
            print(f"{word_hunt} | количество жизней:{count_lives}")
            slovo = str(input('Назовите букву или слово целиком: '))
            proverka = []

            if slovo == word:
                print('Вы выиграли')
                record += 1
                break

            if slovo in word:
                for i in range(len(word)):
                    if slovo == word[i]:
                        proverka.append(i)
                for i in proverka:
                    word_hunt = word_hunt[:i] + slovo + word_hunt[i + 1:]
            elif len(slovo) == len(word) and slovo != word:
                print('Слово неправильное! Вы проиграли')
                break
            else:
                print('\nОшибка! Наверное, вы ввели не ту букву, или она уже есть в слове'
                      '\n-1 жизнь')
                count_lives -= 1

            if word_hunt == word:
                print(f"Вы выиграли. Загаданное слово: {word}\n")
                record += 1
                break


            if count_lives == 0:
                print('Ваши жизни закончились! Вы проиграли')
                get_record(record)
                break


        if count_lives != 0:
            next_game = next_time()
            if next_game == 1:
                game(lives, word_list, record)
            else:
                get_record(record)
                print('До свидания!')
        else:
            print("До свидания")




