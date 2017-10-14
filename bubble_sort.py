''' Bubble Sort Algorithm '''

def bubble_sort(aList):
    temp = ''
    for index in range(len(aList)-1):
        if aList[index] > aList[index+1]:
            temp = aList[index]
            aList[index] = aList[index+1]
            aList[index+1] = temp
            bubble_sort(aList)
    return aList

print(bubble_sort([2,1,5,4,199]))