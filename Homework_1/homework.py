# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

numbers = [79, 96, 71, 5, 69, 95, 78, 48, 30, 14]


def sort_list_imperative(numbers):
    # Императивный код
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j +1], numbers[j]
    return numbers


def sort_list_declarative(numbers):
    # Декларативный код
    numbers.sort(reverse=True)


if __name__ == "__main__":
    print(sort_list_imperative(numbers))
    sort_list_declarative(numbers)
    print(numbers)
