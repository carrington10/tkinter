from tkinter import *
def add_item():
    print("add item")

def remove_item():
    print("add item")

def update_item():
    print("add item")

def clear_item():
    print("add item")
app = Tk()
app.title("Store Manager")


app.geometry("700x350")
# item
item_text = StringVar()
item_label = Label(app,text="Item name",font=('bold',14),pady=20,padx=20)
item_label.grid(row=0,column=0,sticky=W)
item_entry = Entry(app,textvariable=item_text)
item_entry.grid(row=0,column=1);
# customer
customer_text = StringVar()
customer_label = Label(app,text="Customer",font=('bold',14),pady=20,padx=20)
customer_label.grid(row=0,column=2);
customer_entry = Entry(app,textvariable=customer_text)
customer_entry.grid(row=0,column=3,sticky=W)
#seller
seller_text = StringVar()
seller_label = Label(app,text="Seller",font=('bold',14),pady=20,padx=20)
seller_label.grid(row=1,column=0,sticky=W)
seller_entry = Entry(app,textvariable=seller_text)
seller_entry.grid(row=1,column=1);
#price
price_text = StringVar()
price_label = Label(app,text="Price",font=('bold',14),pady=20,padx=20)
price_label.grid(row=1,column=2);
price_entry = Entry(app,textvariable=price_text)
price_entry.grid(row=1,column=3,sticky=W)

add_btn = Button(app,text='Add order',width=12,command=add_item)
add_btn.grid(row=2,column=0,pady=20)

remove_btn = Button(app,text='Remove button',width=12,command=remove_item)
remove_btn.grid(row=2,column=1,pady=20)

update_btn = Button(app,text='update order',width=12,command=update_item)
update_btn.grid(row=2,column=2,pady=20)

clear_btn = Button(app,text='Remove button',width=12,command=clear_item)
clear_btn.grid(row=2,column=3,pady=20)

app.mainloop();