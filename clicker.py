from tkinter import *
app = Tk();
app.title("Clicker")

app.geometry("300x100")

click_text = StringVar();
click_text.set("Clicks: 0")
click_label = Label(app,textvariable=click_text)
click_label.pack();

app.mainloop();