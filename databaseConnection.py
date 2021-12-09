import sqlite3

con = sqlite3.connect(database=r'tbs.db')
cur = con.cursor()

def create_db():
    
    cur.execute("CREATE TABLE IF NOT EXISTS registration(reg_id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(100),address VARCHAR(100),gender VARCHAR(100),email VARCHAR(100),telephone VARCHAR(100),password VARCHAR(100),userType VARCHAR(100),licence VARCHAR(100), status VARCHAR(100))")
    con.commit()

    cur.execute("Insert into registration (name,address,gender,email,telephone,password,userType) values ('admin','kmt','male','admin@gmail.com','9852136542','admin','Employee')")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS customer(c_id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(100),address VARCHAR(100),gender VARCHAR(100),email VARCHAR(100),telephone VARCHAR(100),password VARCHAR(100),userType VARCHAR(100),creditCard VARCHAR(100))")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS booking(booking_id INTEGER PRIMARY KEY AUTOINCREMENT, picDate VARCHAR(100), dropDate VARCHAR(100), picTime VARCHAR(100), dropTime VARCHAR(100), picAddress VARCHAR(100), dropAddress VARCHAR(100), status VARCHAR(100), cancel VARCHAR(20), reg_id INTEGER,c_id INTEGER, CONSTRAINT fk_registration FOREIGN KEY (reg_id) REFERENCES registration(reg_id), CONSTRAINT fk_customer FOREIGN KEY (c_id) REFERENCES customer(c_id))")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS receipt(bill_No INTEGER PRIMARY KEY AUTOINCREMENT, rate VARCHAR(100), km VARCHAR(100), total VARCHAR(100), sc VARCHAR(100), vat VARCHAR(100), grandTotal VARCHAR(100),c_id INTEGER, CONSTRAINT fk_customer FOREIGN KEY (c_id) REFERENCES customer(c_id))")
    con.commit()
                                                                                                                                                                        
create_db()
