import time

def bubble_sort(array, drawData, timeTick):
  isSorted = False
  counter = 0
  while not isSorted:
    isSorted = True
    for i in range(len(array) - 1 - counter):
      if array[i] > array[i + 1]:
        array[i], array[i + 1] = array[i + 1], array[i]   # Swap values if they're not sorted
        isSorted = False

        # '#FFB51E' = purple ==> base arrayColor
        # '#D500FF' = orange ==> items we're currently checking
        drawData(array, ['#FFB51E' if x == i or x == (i + 1) else '#D500FF' for x in range(len(array))])
        time.sleep(timeTick)

    counter += 1
  drawData(array, ['#00FF66' for x in range(len(array))])   # arrayColor once it's all sorted

  



# ----------- TEST -----------
# data = [2, 3, 5, 1, 4, 0]
# data = bubble_sort(data)
# print(data)