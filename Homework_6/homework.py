# Домашнее задание
# Бинарный поиск
# * Контекст
# Предположим, что мы хотим найти элемент в массиве (получить его индекс). 
# Мы можем это сделать просто перебрав все элементы.
# Но что, если массив уже отсортирован? В этом случае можно использовать бинарный поиск. 
# Принцип прост: сначала берём элемент находящийся посередине и сравниваем с тем, который мы
# хотим найти. Если центральный элемент больше нашего, рассматриваем массив слева от центрального, 
# а если больше - справа и повторяем так до тех пор, пока не найдем наш элемент.
# * Ваша задача
# Написать программу на любом языке в любой парадигме для бинарного поиска. 
# На вход подаётся целочисленный массив и число. 
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.



import bisect


def binary_search__functional(list_, target):
    result = bisect.bisect_left(list_, target)
    if result < len(list_) and list_[result] == target:
        return result
    else:
        return -1


my_list = [2, 3, 4, 5, 6, 7, 8, 9]

target = 8
result = binary_search__functional(my_list, target)
print(result)
# result = 6

target = 12
result = binary_search__functional(my_list, target)
print(result)
# result = -1
# Так как 12 больше наибольшого элемента в списке, то bisect_left возвращает индекс len(list_) + 1, то есть 
# при проверке условия "if result < len(list_)" получаем False и переходим на "else: return -1"

target = 1
result = binary_search__functional(my_list, target)
print(result)
# result = -1
# Так как 1 меньше самого наименьшего элемента в списке, то bisect_left возвращает индекс 0, то есть 
# при проверке условия "if list_[result] == target" получаем False и переходим на "else: return -1"
