from time import sleep

text_list = []

with open('dayry.txt') as file:
    for item in file:
        text_list.append(item)

for i in text_list:
    for el in i:
        print(i, end='')
        sleep(0.2)
