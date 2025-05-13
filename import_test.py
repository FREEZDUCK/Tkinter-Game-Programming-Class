from tkinter import *
from apple_type import *

app = Tk()
app.title('사과게임')
app.geometry("1280x760")
app.resizable(False, False)

canvas = Canvas(width=1280, height=760, bg='white')
canvas.place(x=-2, y=-2)

test_i = PhotoImage(file="sample_apple.png")
canvas.create_image(200, 300, image=test_i)

def press_b(key):
    print("B키가 눌렸다")

app.bind('<b>', press_b)

app.mainloop()