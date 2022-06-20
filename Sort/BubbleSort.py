def bubbleSort(list):
    size = len(list)-1
    for i in range(size,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1], list[j]
    return list
arr = [50,23,67,14,64,37,63,96,35,19]

print(bubbleSort(arr))