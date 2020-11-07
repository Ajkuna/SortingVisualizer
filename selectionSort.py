import time

def selection_sort(array, drawData, timeTick):
  currentIdx = 0
  while currentIdx < len(array) - 1:
    smallestIdx = currentIdx
    for i in range(currentIdx + 1, len(array)):
      if array[smallestIdx] > array[i]:
        smallestIdx = i

    drawData(array, ['#2EC1FF' if x == currentIdx else '#FFB51E' if x == smallestIdx else '#D500FF' for x in range(len(array))])
    time.sleep(timeTick)

    swap(currentIdx, smallestIdx, array)
    currentIdx += 1
  
  drawData(array, ['#00FF66' for x in range(len(array))])

def swap(i, j, array):
  array[i], array[j] = array[j], array[i]





# ----------- TEST -----------
# data = [2, 3, 5, 1, 4, 0]
# data = selection_sort(data)
# print(data)