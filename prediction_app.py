#!/usr/bin/env python
# coding: utf-8

import random
answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.', 'Как Вас зовут?', sep='\n')
name=(input('Введите имя:'))
print(f'Привет, {name}!')
while True:
    q = input('Задайте вопрос:')
    print(random.choice(answers))
    print('Хотите задать еще один вопрос? да//нет')
    ans = input()
    if ans == 'да':
        continue
    elif ans == 'нет':
        break
print('Возвращайся если возникнут вопросы!')

