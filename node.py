class Node():                   # Запись (элемент) списка
 
    def __init__(self, data,prev, next): 
        self.data = data        # данные
        self.prev = prev      #указатель на предыдущий элемент
        self.next = next      #указатель на следующий элемент