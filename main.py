from doublelist import DoubleLinkedList

new_list=DoubleLinkedList() 			#создаем объект

while True:               				#входим в цикл и выводим меню взаимодействия
	print("1-Добавить элемент в начало списка\n"+
	"2-Добавить элемент в конец списка\n"+
	"3-Добавить элемент в список перед узлом со значением (в списке должно быть хотя бы 1 значеие)\n"+
	"4-Удалить элемент в начале списка\n"+
	"5-Удалить элемент в конце списка\n"+
	"6-Удалить элемент из списка по индексу\n"+
	"7-Проверка пустоты\n"+
	"8-Вывод списка\n"+
	"9-Уничтожение списка\n"+
	"0-Выход\n")
	print("-"*50)

	choose=int(input("Chose option: "))  				#считываем выбор пользователя
	if choose == 1:										#и выполняем условие, согласно выбору
		new_list.addToHead(int(input("Enter data: ")))
	elif choose == 2:
		new_list.addToTail(int(input("Enter data: ")))
	elif choose == 3:
		if new_list.isEmpty is False:
			new_list.listInsert(int(input("Enter data ")), int(input("Enter requiest ")))
		else:
			print("List is empty")
	elif choose == 4:
		new_list.delFromHead()
	elif choose == 5:
		new_list.delFromTail()
	elif choose == 6:
		new_list.delByNum(int(input("Enter index: ")))
	elif choose == 7:
		new_list.isEmpty()
	elif choose == 8:
		new_list.listOut()
	elif choose == 9:
		new_list.destroyList()
	elif choose == 0:
		break
	print("-"*50)
