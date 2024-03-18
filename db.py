import sqlite3
# creates the table
sql_create = '''
CREATE TABLE IF NOT EXISTS  orders
(id INTEGER primary KEY,
 item text,
 customer text,
 seller text,
 price text);
'''
sql_insert = "insert into orders values (null,?,?,?,?)"

sql_fetch = 'select * from orders'

sql_remove = 'delete from orders where id=?'

sql_update = 'update orders set item=?,customer=?,seller=?,price=? where id=?'

# databse class 
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db);
        self.cursor = self.conn.cursor();
        self.cursor.execute(sql_create)

    def insert(self,item,customer,seller,price):
        self.cursor.execute(sql_insert,(item,customer,seller,price))
        self.conn.commit();
    
    def remove(self,id):
        self.cursor.execute(sql_remove,(id,))
        self.conn.commit();

    def update(self,id,item,customer,seller,price):
        self.cursor.execute(sql_update,(id,item,customer,seller,price))
        self.conn.commit();
    
    def fetch(self):
        self.cursor.execute(sql_fetch)
        return self.cursor.fetchall();

    def __del__(self):
        self.cursor.close();

db = Database('store.db')
db.insert('laptop','jane','apple','1400');
db.insert('phone','camron','android','999');
db.insert('playstation 5','jade','sony','500');

print(db.fetch());