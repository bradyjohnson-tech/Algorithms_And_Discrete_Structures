def selection_sort(a):
    for i in range(len(a)-1):
        minIndex = i
        for j in range(i+1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]


        

