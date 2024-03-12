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









# databse class 
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db);
        self.cursor = self.conn.cursor();
        self.cursor.execute(sql_create)

    
    def fetch(self):
        self.cursor.execute(sql_fetch)
        return self.cursor.fetchall();

    def __del__(self):
        self.cursor.close();

db = Database('store.db')
db.fetch()