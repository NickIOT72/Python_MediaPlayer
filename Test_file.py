import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
x = file_path.split(".")
y = file_path.split("/")
y1 = y[len(y) -1]
y2 = y1.split(".")
filename = y2[0]
print(filename)
if (x[len(x) -1] == "mp3"):
    print("Es mp3")
    print(x)
else:
    print("no es mp3")