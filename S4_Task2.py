print("\033[H\033[J", end="")
"""
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore
I'm sure that the shells are sea shore shells
Output: 13
"""
input_string = 'Я один, а ты ты два, а он он он три , а она она она она четыре, а оно оно оно оно оно пять.'.lower().split()

print(len(set(input_string)))