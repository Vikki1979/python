# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

def index_element(array, min, max):
    index_element = []
    for i in range(len(array)):
        if min <= array[i] <= max:
            index_element.append(i)
    return index_element

def random_array(n):
    array1 = []
    for i in range(n):
        array1.append(random.randint(1,10))
    return array1

count = int(input("Введите количество элементов массива: "))    
list_main = random_array(count)
print(f'Получен массив: {list_main}')
min_element = int(input("Минимальное значение элемента массива: "))
max_element = int(input("Максимальное значение элемента массива: "))
list2 = index_element(list_main, min_element, max_element)
print(f'Индексы элементов массива: {list2}')
