import tkinter as tk


class DragRectangle:
    def __init__(self, canvas, x1, y1, x2, y2, color="blue"):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.canvas.tag_bind(self.id, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.id, "<ButtonRelease-1>", self.on_release)
        self.canvas.tag_bind(self.id, "<B1-Motion>", self.on_motion)

    def on_press(self, event):
        self.x = event.x
        self.y = event.y

    def on_release(self, event):
        pass

    def on_motion(self, event):
        dx = event.x - self.x
        dy = event.y - self.y
        self.canvas.move(self.id, dx, dy)
        self.x = event.x
        self.y = event.y

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

rect = DragRectangle(canvas, 50, 50, 100, 100)

root.mainloop()