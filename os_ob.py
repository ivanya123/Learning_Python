with open("primer.txt", 'r') as f:
    data = f.readlines()

sort_data = sorted((int(s.strip()) for s in data), reverse=True)

print(sort_data)
