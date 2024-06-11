print("\033[H\033[J", end="")

# for i in 'hello world':
#     if i == 'a':
#         break
# else:  # Причём интересно что else здесь работает, только если в for не было ни одного вхождения в if  (или надо уточнить).
#     print('Буквы a в строке нет')

print()
print('\t Начало рекурсии:')

def func(my_str='Hedgehog', count = 1):
    print(f'\t   Текущая Итерация f-ции №{count}:')
    if len(my_str) != 0:
        if my_str[0] != 'a':
            print(f' Вход в if. Длина строки осталась L{len(my_str)}.')
            func(my_str[1:], count + 1)
        print('Обнаружена "a".') # удалить. Либо поставить под else. Но тогда после принта "Буквы "a" нет." нужен ещё 1 exit().
        exit()  #break
    print(f'Выход из тела f-ции №{count}.\t И Буквы "a" в строке нет.')
func()