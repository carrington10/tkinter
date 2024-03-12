from tkinter import *
from db import Database
db = Database('store.db')
selected_item = ''

def populate_list():
    order_list.delete(0,END)
    for row in db.fetch():
        order_list.insert(END,row);
def add_item():
    if not item_text.get() or not customer_text.get() or not seller_text.get() or price_text.get():
            item = item_text.get()
            customer = customer_text.get()
            seller = seller_text.get()
            price = price_text.get()
            db.insert(item,customer,seller,price);


def remove_item():
    print("delete_item")
def update_item():
    print("add item")

def clear_item():
    item_entry.delete(0,END)
    customer_entry.delete(0,END)
    seller_entry.delete(0,END)
    price_entry.delete(0,END)
    selected_item = ''
app = Tk()
app.title("Store Manager")

def select_item(item):
    clear_item();
    print("select item")
    global selected_item 
    index = order_list.curselection()[0]
    selected_item = order_list.get(index)
    print(selected_item)
    item_entry.insert(END,selected_item[1])
    customer_entry.insert(END,selected_item[2])
    seller_entry.insert(END,selected_item[3])
    price_entry.insert(END,selected_item[4])
    

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

clear_btn = Button(app,text='Clear button',width=12,command=clear_item)
clear_btn.grid(row=2,column=3,pady=20)

order_list = Listbox(app,height=5,width=50,borderwidth=1)
order_list.grid(row=3,column=0,columnspan=3,rowspan=6,padx=20,pady=20)

scroll = Scrollbar(app,orient=VERTICAL,command=order_list.yview)
scroll.grid(row=3,column=2,rowspan=6,sticky=E,padx=20)

order_list.configure(yscrollcommand=scroll.set)
order_list.bind("<<ListboxSelect>>", select_item)

populate_list();
app.mainloop();