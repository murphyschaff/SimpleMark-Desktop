import tkinter as tk
from tkinter import *
import datetime

def save(year, monthTxt, day, hr, min, hrType):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    month = 0
    for i in range(len(months)):
        if months[i] == monthTxt:
            month = i + 1

    time = datetime.datetime(year, month, day, hr, min)
    checkTime = datetime.datetime(1999, 1, 1, 1, 1)
    print(time > checkTime)



window = tk.Tk()

frame = tk.Frame()
frame.pack()

hrEntry = tk.Entry(
    master=frame,
    width=10
)
minEntry = tk.Entry(
    master=frame,
    width=10
)
yearEntry = tk.Entry(
    master=frame,
    width=20
)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
days = list(range(1,32))


twelveHr = ["AM", "PM"]

monthType = StringVar()
monthType.set(months[0])
dayType = IntVar()
dayType.set(days[0])
hrType = StringVar()
hrType.set(twelveHr[0])

yearEntry.pack()

monthOption = OptionMenu(frame, monthType, *months)
monthOption.pack()

dayOption = OptionMenu(frame, dayType, *days)
dayOption.pack()

hrEntry.pack()
minEntry.pack()
hrOption = OptionMenu(frame, hrType, *twelveHr)
hrOption.pack()

saveButton = tk.Button(
    master=frame,
    width=5,
    text="save",
    command=lambda: save(int(yearEntry.get()), monthType.get(), dayType.get(), int(hrEntry.get()), int(minEntry.get()),
                         hrType.get())
)
saveButton.pack()
window.mainloop()

