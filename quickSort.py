import time

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)


    #swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]
    
    return border

def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)

        # LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawData, timeTick)

        # RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawData, timeTick)



def getColorArray(dataLen, head, tail, border, currIdx, isSwapping = False):
    colorArray = []
    for i in range(dataLen):

        # Base coloring
        if i >= head and i <= tail:
            colorArray.append('#AF69B2')
        else:
            colorArray.append('#FD9CFF')

        if i == tail:
            colorArray[i] = '#2E4AFF'
        elif i == border:
            colorArray[i] = '#FF2EA5'
        elif i == currIdx:
            colorArray[i] = '#2EC1FF'

        if isSwapping:
            if i == border or i == currIdx:
                colorArray[i] = '#D500FF'

    return colorArray




# ----------- TEST -----------
# data = [2, 3, 5, 1, 4, 0]
# data = quickSort(data)
# print(data)