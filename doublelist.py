from node import Node                           #подключение класса Node
class DoubleLinkedList():
 
    def __init__(self):
        self.head = None                        #указатель на начало
        self.tail = None                        #указатель на конец
        self.count=0




    def addToHead(self, data):                  #добавление в начало
        new_data = Node(data, None, None)       #создаем запись
        if self.head is None:                   #если список пустой, то новый элемент будет->
            self.head =self.tail = new_data     #-> концом и началом одновременно
        else:
            self.head.prev=new_data             #иначе указатель с хвоста и с начала 
            self.tail.next=new_data             #указывает на новую запись, а указатели новой
            new_data.next=self.head             #записи теперь указыают на начало и конец
            new_data.prev=self.tail
            self.head=new_data                  #новый головной элемент теперь вновь добавленный
        self.count+=1                           #прибавляем 1 к количеству записей в списке




    def addToTail(self, data):                  # добавление в конец
        new_data=Node(data, None, None)         #если список пустой, то новый элемент будет->
        if self.tail is None:                   # -> концом и началом одновременно
            self.head =self.tail = new_data
        else:
            new_data.next=self.head             #иначе указатель с хвоста и с начала 
            new_data.prev=self.tail             #указывает на новую запись, а указатели новой
            self.tail.next=new_data             #записи теперь указыают на начало и конец
            self.head.prev=new_data
            self.tail=new_data                  #новый хвостоой элемент теперь вновь добавленный
        self.count+=1                           #прибавляем 1 к количеству записей в списке




    def listInsert(self,data,request):          #добавление перед узлом с указаным значением
        new_data=Node(data, None, None)
        curr=self.head                          #ставим указатель на начало списка
        x=1
        while x<=self.count:                    #пока указатель не дойдет до конца:
            if curr.data == request:            #ищем ячейку с индексом
                if self.count==1:               #если такая ячейка 1 то, добавляем запись в начало 
                    self.head.prev=new_data
                    self.tail.next=new_data
                    new_data.next=self.head
                    new_data.prev=self.tail
                    self.head=new_data
                    break
                else:                           #иначе добавляем запись между двумя другими
                    temp=curr.prev              #и корректируем указатели 
                    curr.prev=new_data 
                    temp.next=new_data
                    new_data.next=curr
                    new_data.prev=temp
                    break                           
            curr=curr.next
        self.count+=1                           #прибавляем 1 к количеству записей в списке




    def destroyList(self):              #уничтожение списка
        print("Destroing"+"."*7)
        if self.head is None:           #проверка на пустоту
            print("List is empty")
        else:
            curr=self.head.next         #иначе, удаляем элементы по очереди, пока они не закончатся
            while self.count>0:         #используя цикл while
                if self.count == 1:
                    self.head=None
                    self.tail=None
                else:
                    del_elem=curr.prev
                    curr.prev=self.tail
                    self.tail.next=curr
                    self.head=curr
                    del_elem.data=None
                    del_elem.next=del_elem.prev=None
                    curr=curr.next
                    del del_elem
                self.count-=1




    def isEmpty(self):                  #проверка на пустоту
        if self.head is None:
            print("List is empty")
            return True
        else:
            print("List is not Empty")
            return False




    def delFromHead(self):              #удаление из начала списка
        if self.count == 1:
            self.head=None
            self.tail=None
        else:
            curr=self.head                  #ставим указатель на начало списка
            new_head=curr.next              #смещаем указатель на один элемент вправо
            new_head.prev=self.tail         #далее меняем указатели на выбранный элемент
            self.tail.next=new_head         #теперь все указатели ссылаются на новый головной
            curr.data=None                  #очищаем данные и указатели бывшего первого элемента
            curr.next=curr.prev=None
            self.head=new_head              #теперь первый элемент это бывший второй
        self.count-=1                   #уменьшаем длинну списка на 1




    def delFromTail(self):              #удаление из конца списка
        if self.count == 1:
                    self.head=None
                    self.tail=None
        else:
            curr=self.tail                  #ставим указатель на конец списка
            new_tail=curr.prev              #смещаем указатель на один элемент вправо
            new_tail.next=self.head         #далее меняем указатели на выбранный элемент
            self.head.prev=new_tail         #теперь все указатели ссылаются на новый хвостовой
            curr.data=None                  #очищаем данные и указатели бывшего первого элемента
            curr.next=curr.prev=None
            self.tail=new_tail              #теперь последний элемент это бывший предпоследний
        self.count-=1                   #уменьшаем длинну списка на 1




    def delByNum(self, index):          #удаление элемента по его индексу
        curr=self.head                  #ставим указатель на начало списка
        x=1
        while True :                    #пока цикл выполняется идет поиск нужного индекса
            if x == index:              #если такой найден, то смещаем указатель на 1 элемент вправо
                if curr is self.head:
                    if self.count == 1:
                        self.head=None
                        self.tail=None
                        break
                    else:
                        curr=self.head                  #ставим указатель на начало списка
                        new_head=curr.next              #смещаем указатель на один элемент вправо
                        new_head.prev=self.tail         #далее меняем указатели на выбранный элемент
                        self.tail.next=new_head         #теперь все указатели ссылаются на новый головной
                        curr.data=None                  #очищаем данные и указатели бывшего первого элемента
                        curr.next=curr.prev=None
                        self.head=new_head              #теперь первый элемент это бывший второй
                        break
                else:
                    temp=curr.prev     #корректируем указатели так, чтобы два сосдених от индекса
                    next_temp=curr.next
                    temp.next=next_temp       #элемента указывали друг на друга 
                    next_temp.prev=temp
                    curr.data=None                 #очищаем данные и указатели бывшего нужного элемента
                    curr.next=curr.prev=None
                    del curr
                    break                   #выходим из цикла
            curr=curr.next
            x+=1
        self.count-=1               #уменьшаем длинну списка на 1




    def listOut(self):                  #вывод списка
        print("Printing"+"."*7)
        if self.head is None:         #если список пустой, то выводим сообщение
            print("List is Empty")
        else:                         #иначе проходим по списку циклом while и выводим на экран
            curr=self.head
            x=1
            while x <= self.count:
                print(curr.data)
                curr=curr.next
                x+=1
        print("Done!")