a = int(input("Введите число"))
my_list = [1, 2] #Это начальные числа, так что отсчет идет после 2
for i in range(a):
    my_list.append(my_list[-1] + my_list[-2])
    my_list.pop(0)
my_list.pop(0)
print(my_list)