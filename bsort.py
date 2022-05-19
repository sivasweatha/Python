data = [5, 7, 3, 2, 4, 0]

j = 0
while j < len(data):
    i = 0
    while i < len(data) - 1:
        if data[i] > data[i+1]:
            temp = data[i+1]
            data[i+1] = data[i]
            data[i] = temp
        i += 1
    j += 1

print(data)