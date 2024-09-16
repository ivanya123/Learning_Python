n = int(input())
list_process = [input().split() for _ in range(n)]


def time_process(time: int, *dependencies: str):
    if dependencies:
        max_dependency_time = 0
        for dep in dependencies:
            dependency_time = time_process(int(list_process[int(dep) - 1][0]), *list_process[int(dep) - 1][1:])
            max_dependency_time = max(max_dependency_time, dependency_time)
        return time + max_dependency_time
    else:
        return time


list_time = []

for i, *index in list_process:
    list_time.append(time_process(int(i), *index))

print(max(list_time))
