def main():
    last_keyword = input()
    unique_chars= input()
    len_password = int(input())
    for i in unique_chars:
        if i not in last_keyword:
            return -1

    for i in range(len(last_keyword) - len_password + 1):
        flag = True
        for j in unique_chars:
            if j not in last_keyword[-len_password:]:
                flag = False
                break

        if flag:
            return last_keyword[-len_password:]

        last_keyword = last_keyword[:-1]

    return -1


print(main())
