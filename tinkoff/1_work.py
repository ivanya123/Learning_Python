string = input()

list_d = string.split(',')

for i in list_d:
    if '-' in i:
        for j in range(int(i[0]), int(i[2])+1):
            print(j, end =' ')
    else:
        print(int(i), end =' ')