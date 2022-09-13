# вывод всех записей подряд побуквенно.
from time import sleep

text_list = []

with open('dayry.txt') as file:
    for item in file:
        text_list.append(item)

for i in text_list:
    for el in i:
        print(i, end='')
        sleep(0.2)

# создаю список всех записей.
file_diary = open("dayry.txt")
diary_text = file_diary.read()
file_diary.close()
split_diary = diary_text.split('___')

# Вывод случайного задания и случайной записи дневника
import random

file = open("ITDO.txt")
text = file.read()
file.close()
split_text = text.split('><')

file_diary = open("dayry.txt")
diary_text = file_diary.read()
file_diary.close()
split_diary = diary_text.split('___')

number = random.randint(0, len(split_text))
print(split_text[number])

number_note = random.randint(0, len(split_diary))
print(split_diary[number_note])
