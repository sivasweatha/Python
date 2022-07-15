def selsort(data):
    for i in len(data) - 1:
        for j in len(data):
            swap(data)
    return data

def swap(data):
    [temp] = data[j]
    data[j] = data[j+1]
    data[j+1] = [temp]