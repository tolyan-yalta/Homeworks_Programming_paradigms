# * Условие
# На вход подается число n.
# * Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

n = 7


def table_band(min_value, max_value, n):
    for i in range(1, n + 1):
        for j in range(min_value, max_value):
            print(f"{j} X {i}{'' if i == 10 else ' '}={('  ' if j * i < 10 else ' ')}{j * i}\t", end='')
        print()
    print()
    

print(' ' * 29 + 'ТАБЛИЦА УМНОЖЕНИЯ')
table_band(1, 6, n)
table_band(6, 11, n) 

# Скрипт написан в парадигме процедурного программирования (вызывается функция которая ничего не возвращает).
# Это позволяет выводить таблицу умножения блоками (например с 1 до 5 и с 6 до 10) не повторяя код.
