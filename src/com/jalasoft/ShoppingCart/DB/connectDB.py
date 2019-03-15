import os
import sqlite3

"""This class will allow as to have a DB conection using sqlite3
It is required to provide the db name
"""


class ConnectionDB:
    databaseName = "ShoppingCart.db"

    def __init__(self):
        self.exist = os.path.exists(self.databaseName)

    """metodh to get the connection with db, some tables were created by default"""

    def getConnection(self):
        conn = sqlite3.connect(self.databaseName)
        if not self.exist:
            c = conn.cursor()
            c.execute(
                """create  table if not exists items(itemid integer primary key  autoincrement,itemname varchar(100), description varchar(200) not null , price real not null , stock integer not null , categoryid integer not null ,foreign key(categoryid) references categories(categoryid))""")
            c.execute(
                """create  table if not exists categories(categoryid integer primary key not null, name varchar(200) not null)""")
            c.execute(
                """create  table if not exists users(userid integer primary key  autoincrement, username varchar(100) not null, password varchar(100) not null,email varchar(100) not null, firstname varchar(100) not null, lastname varchar(100) not null, phonenumber integer )""")
            c.execute(
                """create  table if not exists cart(cartid integer not null, userid integer not null,itemid integer not null,quantity integer not null,price real not null, foreign key(userid) references users(userId),foreign key(itemid) references items(itemid))""")

            c.execute("""insert into categories values(1, "Men")""")
            c.execute("""insert into categories values(2, "Women")""")
            c.execute("""insert into items values(Null, 'T-Shirt1', 'description T-Shirt1', 2, 5, 2)""")
            c.execute("""insert into items values(Null, 'T-Shirt2', 'description T-Shirt2', 3, 15, 2)""")
            c.execute("""insert into items values(Null, 'Dress1','description Dress1', 10, 10, 2)""")
            c.execute("""insert into items values(Null, 'T-Shirt1', 'Descrition T-Shirt1', 22, 15, 1)""")
            c.execute("""insert into items values(Null, 'Jacket1', 'description Jacket1', 20, 25, 1)""")
            c.execute("""insert into items values(Null, 'Shoes', 'description Shoes', 50, 50, 1)""")
            c.execute(
                """insert into users values(Null, 'mfuentes', 'control123', 'mfuentes@test.com', 'Magali', 'Fuentes', 67532680)""")

            conn.commit()


        return conn


c = ConnectionDB()
c.getConnection()

