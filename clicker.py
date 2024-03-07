from tkinter import *
count = 0;

def get_string():
    global count;
    return f"clicks: {count}"

def btn_click():
    global count
    count+=1;
    click_text.set(get_string());

def btn_reset():
    global count
    count = 0;
    click_text.set(get_string())


app = Tk();
app.title("Clicker")

app.geometry("300x100")

click_text = StringVar();
click_text.set("Clicks: 0")
click_label = Label(app,textvariable=click_text)
click_label.pack();
click_btn = Button(app,text="click", width=12,command=btn_click)
click_btn.pack();

reset_btn = Button(app,text="reset", width=12,command=btn_reset)
reset_btn.pack();
app.mainloop();