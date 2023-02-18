import tkinter as tk

root = tk.Tk()
root.title("Two Blocks")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

block1 = canvas.create_rectangle(100, 100, 300, 200, fill="red")
block2 = canvas.create_rectangle(400, 100, 600, 200, fill="blue")

root.mainloop()

