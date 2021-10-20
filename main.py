from random import randint
from functions import *

LENGTH = 10
list = []

for i in range(LENGTH):
    list.append(randint(0, 16))

print("Начальный список:", list)
print("Отсортированный список:", sort(list))
print("Индекс первого элемента со значением 8:", indexOf(8, list))
print("Пять наименьших элементов списка:", getMinFive(list))
print("Пять наибольших элементов списка:", getMaxFive(list))
print("Среднее арифметическое:", getAvg(list))
print("Неповторяющиеся элементы списка:", getUnique(list))
print("Количество неуникальных элементов списка:", getNotUniqueCount(list))
print("Сдвинутый массив:", shiftList(list))