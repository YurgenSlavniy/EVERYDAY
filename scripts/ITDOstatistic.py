import random

file = open("D:/IT_WORKSHOP/github_everyday/ITDO.txt")
text = file.read()
file.close()

split_text = text.split('><')
ends = []
noends = []
mainf = []
scriptsf = []

for el in split_text:
    if "+" in el:
        ends.append(el)
    else:
        noends.append(el)

for el in split_text:
    if "!!!" in el:
        mainf.append(el)

for el in split_text:
    if "НАПИСАТЬ СКРИПТ" in el:
        scriptsf.append(el)

print(f'всего заданий: {len(split_text)}\n'
      f'выполненные задания: {len(ends)} \n'
      f'невыполненные: {len(noends)} \n'
      f'заданий с !!!: {len(mainf)}\n'
      f'заданий НАПИСАТЬ СКРИПТ: {len(scriptsf)}')


