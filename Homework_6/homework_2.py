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
# !!!  Исключая функциональную. Только в императивной парадигме? !!!
# На вход подаётся целочисленный массив и число. 
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.



def binary_search_recursive(sort_list, target, start, end):
    if start > end:
        return -1
    middle = (start + end) // 2
    if sort_list[middle] == target:
        return middle
    elif sort_list[middle] < target:
        temp_res = binary_search_recursive(sort_list, target, middle + 1, end)
        return temp_res
    else:
        temp_res = binary_search_recursive(sort_list, target, start, middle - 1)
        return temp_res


def binary_search(sort_list, target):
    if len(sort_list) == 0:
        return -1
    middle = len(sort_list) // 2
    if sort_list[middle] == target:
        return middle
    elif sort_list[middle] < target:
        return binary_search_recursive(sort_list, target, middle + 1, len(sort_list) - 1)
    else:
        return binary_search_recursive(sort_list, target, 0, middle)
    

my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

target = 12
result = binary_search(my_list, target)
print(result)
# result = 10

target = 4
result = binary_search(my_list, target)
print(result)
# result = 2

target = 8
result = binary_search(my_list, target)
print(result)
# result = 6

target = 1
result = binary_search(my_list, target)
print(result)
# result = -1

target = 15
result = binary_search(my_list, target)
print(result)
# result = -1