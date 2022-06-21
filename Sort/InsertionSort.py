def insertSort(list):
    for i in range(1, len(list)):
        j = i-1
        item = list[i]
        while(list[j] > item) and (j>=0):
            list[j+1] = list[j]
            j = j-1
        list[j+1] = item
    return list
arr = [50,23,67,14,64,37,63,96,35,19]

print(insertSort(arr))