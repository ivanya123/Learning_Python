days = int(input('Введите кол-во  дней '))
journal_entry = input('Введите запись из журнала ')

list_height = [int(i) for i in journal_entry.split() if i != '-1']
flag = True
for index, i in enumerate(list_height[:-1]):
    if i > list_height[index+1]:
        print("NO")
        flag = False
        break
if flag:
    print("YES")
    for i in range(1, days+1):
        print(i, end=' ')






