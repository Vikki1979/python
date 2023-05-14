#Заполните массив элементами арифметической прогрессии.
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

def aref_progress(a1, d, n):
    list1 = []
    for i in range(1, n + 1):
        list1.append(a1 + (i-1) * d)
    return list1

first_element = int(input("Введите первый элемент: "))
diff_element = int(input("Введите разность элементов: "))
quantity = int(input("Введите количество элементов: "))
list2 = aref_progress(first_element, diff_element, quantity)
print(f"Получен массив {quantity} элементов арифметической прогрессии: ")
print(list2)