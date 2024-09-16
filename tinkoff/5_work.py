from datetime import timedelta


def minutes_from_time(time_delta: timedelta) -> int:
    return time_delta.seconds // 60


def get_timedelta(string: str) -> timedelta:
    hour, minute, second = string.split(":")
    return timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))


start = input()
n = int(input())
dict_data = {}
list_string = [input().split() for _ in range(n)]
count = 0
for team, time_, server, result in list_string:
    if team not in dict_data:
        dict_data[team] = [0, 0]
    if result == "ACCESSED":
        time_ = get_timedelta(time_) - get_timedelta(start)
        dict_data[team][0] += 1
        dict_data[team][1] += minutes_from_time(time_)
    if result == "DENIED" or result == "FORBIDEN":
        c = 1
        for team1, time_1, server1, result1 in list_string[count + 1:]:
            if team1 == team and server1 == server and (result1 == "DENIED" or result1 == "FORBIDEN"):
                c += 1
            if team1 == team and server1 == server and result1 == "ACCESSED":
                dict_data[team][1] += c * 20
                break
    count += 1

last_list = [[key, value[0], value[1]] for key, value in dict_data.items()]
last_list.sort(key=lambda x: (-x[1], x[2]))
last_list[0].append(1)
for i in range(1, len(last_list)):
    if last_list[i][1] == last_list[i - 1][1] and last_list[i][2] == last_list[i - 1][2]:
        last_list[i].append(last_list[i - 1][-1])
    else:
        last_list[i].append(i+1)

for team, count, minutes, place in last_list:
    print(f'{place} {team} {count} {minutes}')
