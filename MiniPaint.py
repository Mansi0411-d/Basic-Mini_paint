import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Mini Paint")

# Canvas setup
canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

# Brush settings
brush_color = "black"
brush_size = 5

# Draw function
def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)

# Bind mouse movement
canvas.bind("<B1-Motion>", paint)

# Run app
root.mainloop()
