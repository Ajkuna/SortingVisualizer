from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quickSort import quick_sort
from insertionSort import insertion_sort
from selectionSort import selection_sort

root = Tk()
root.title('Sorting Algorithms Visualization')
root.maxsize(920, 620)
root.config(bg='#000045')

# Variables (global)
selected_alg = StringVar()
data = []

def drawData(data, arrayColor):
  canvas.delete("all")
  canvasHeight = 430
  canvasWidth = 900 - (10*2)
  barWidth = canvasWidth / (len(data) + 1)
  offset = 10
  spacing = 8
  
  normalizedData = [ i / max(data) for i in data]
  for i, height in enumerate(data):

    # Top left corner
    x0 = i * barWidth + offset + spacing
    y0 = canvasHeight - height 

    # Bottom right corner
    x1 = (i + 1) * barWidth + offset
    y1 = canvasHeight

    # Data bars
    canvas.create_rectangle(x0, y0, x1, y1, fill=arrayColor[i])
    canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

  root.update_idletasks()
  

def generate():

  global data   # We're accessing the global data

  minValue = int(minEntry.get())
  maxValue = int(maxEntry.get())
  size = int(sizeEntry.get())

  data = []
  for num in range(size):
    data.append(random.randrange(minValue, maxValue))
  
  drawData(data, ['#D500FF' for x in range(len(data))])


def startAlgorithm():
  global data

  if not data:
    return

  if algMenu.get() == 'Quick Sort':
    quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())
    drawData(data, ['#00FF66' for x in range(len(data))])
  elif algMenu.get() == 'Bubble Sort':
    bubble_sort(data, drawData, speedScale.get())
  elif algMenu.get() == 'Insertion Sort':
    insertion_sort(data, drawData, speedScale.get())
  elif algMenu.get() == 'Selection Sort':
    selection_sort(data, drawData, speedScale.get())



# frame / base layout
UI_frame = Frame(root, width = 800, height = 100, bg = '#d5d7ff')
UI_frame.grid(row = 0, column = 0, padx = 0, pady = 10)

# height = (600 - (frame height)) - padding
canvas = Canvas(root, width = 900 - (10*2), height = 440, bg = '#fff')
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)


# --------------- UI AREA -----------------


# VALUES SELECTION (1st row)

# Size selection
# Label(UI_frame, text='Size: ', bg='#d5d7ff').grid(row=1, column=0, padx=5, pady=5, sticky=E)
sizeEntry = Scale(UI_frame, from_=3, to=65, resolution=1, orient=HORIZONTAL, label='Data Size', length=150)
sizeEntry.grid(row=0, column=0, padx=5, pady=5)

# Min-value selection

minEntry = Scale(UI_frame, from_=10, to=90, resolution=10, orient=HORIZONTAL, label='Min Value', length=150)
minEntry.grid(row=0, column=1, padx=5, pady=5)

# Max-value selection

maxEntry = Scale(UI_frame, from_=100, to=400, resolution=25, orient=HORIZONTAL, label='Max Value', length=150)
maxEntry.grid(row=0, column=2, padx=5, pady=5)

# Generate button
Button(UI_frame, text='Generate new array', command=generate, bg='#ffc400').grid(row=0, column=3, padx=5, pady=5)


# ALGORITHM SELECTION (2nd row)
Label(UI_frame, text='Algorithm: ', bg='#d5d7ff').grid(row=1, column=0, padx=5, pady=5, stick=E)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Quick Sort'])
algMenu.grid(row=1, column=1, padx=5, pady=5)
algMenu.current(0)

# Speed scale
speedScale = Scale(UI_frame, from_=0.5, to=0, length=200, digits=2, resolution=0.05, orient=HORIZONTAL, label='Alg. Speed [s]')
speedScale.grid(row=1, column=2, padx=5, pady=5)

# Start button
Button(UI_frame, text='Start', command=startAlgorithm, bg='#18ff2f').grid(row=1, column=3, padx=5, pady=5)






root.mainloop()