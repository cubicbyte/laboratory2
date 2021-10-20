""" Функция сортировки списков """
def sort(list):
    """ Сортировка списка при помощи алгоритма Insertion (Вставка) """
    for i in range(len(list)):
        j = i
        while (list[j] < list[j - 1] and j > 0):
            """ Поменять элементы с индексами j и j-1 местами """
            temp = list[j]
            list[j] = list[j - 1]
            list[j - 1] = temp
            j -= 1
    return sorted(list)

""" Функция для поиска индекса элемента по значению """
def indexOf(element, list):
    """ Перебор всех элементов списка """
    for i in range(len(list)):
        el = list[i]
        if (el == element):
            """ Если нашли элемент, то вернуть его индекс """
            return i
    """ Если не нашли элемент, то вернуть -1 """
    return -1

""" Найти 5 минимальных элементов списка """
def getMinFive(list):
    """ Сортируем список """
    sorted = sort(list)
    fiveMin = []
    """ Записываем и возвращаем 5 минимальных элементов списка """
    for i in range(0, 5):
        fiveMin.append(sorted[i])
    return fiveMin

def getMaxFive(list):
    """ Сортируем список """
    sorted = sort(list)
    fiveMax = []
    """ Записываем и возвращаем 5 максимальных элементов списка """
    for i in range(len(sorted) - 5, len(sorted)):
        fiveMax.append(sorted[i])
    return fiveMax

""" Функция для нахождения среднего арифметического списка """
def getAvg(list):
    avg = 0
    for i in range(len(list)):
        """ Суммируем все элементы списка """
        avg += list[i]
    """ Делим сумму всех элементов списка на их кол-во и возвращаем результат """
    avg /= len(list)
    return avg

""" Функция для нахождения уникальных элементов списка """
def getUnique(list):
    unique = []
    """ Перебор всех элементов списка """
    for i in range(len(list)):
        el = list[i]
        """ Если текущий элемент еще не записывали, то записать """
        if not el in unique:
            unique.append(el)
    return unique