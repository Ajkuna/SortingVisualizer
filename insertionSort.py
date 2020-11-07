import time

def insertion_sort(array, drawData, timeTick):
  for i in range(1, len(array)):
    j = i
    while j > 0 and array[j] < array[j - 1]:
      drawData(array, ['#FFB51E' if x == j or x == (j + 1) else '#D500FF' for x in range(len(array))])
      time.sleep(timeTick)
      swap(j, j - 1, array)
      j -= 1
  
  drawData(array, ['#00FF66' for x in range(len(array))])

def swap(i, j, array):
  array[i], array[j] = array[j], array[i]


  
# ----------- TEST -----------
# data = [2, 3, 5, 1, 4, 0]
# data = insertion_sort(data)
# print(data)