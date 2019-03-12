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

            """Tables that will be used for the cart"""

            c.execute(
                """create  table if not exists items(itemid integer primary key  autoincrement, description varchar(200) not null , price real not null , stock integer not null , categoryid integer not null ,foreign key(categoryid) references categories(categoryid))""")
            c.execute(
                """create  table if not exists categories(categoryid integer primary key not null, name varchar(200) not null)""")
            c.execute(
                """create  table if not exists users(userid integer primary key not null, username varchar(100) not null, password varchar(100) not null,email varchar(100) not null, firstname email varchar(100) not null, lastname email varchar(100) not null)""")
            c.execute(
                """create  table if not exists cart(userid integer not null,itemid integer not null, foreign key(userid) references users(userId),foreign key(itemid) references items(itemid))""")

            """Inserted some data"""

            c.execute("""insert into categories values(1, "Men")""")
            c.execute("""insert into categories values(2, "Women")""")
            c.execute("""insert into items values(Null, 'T-Shirt1', 2, 5, 2)""")
            c.execute("""insert into items values(Null, 'T-Shirt2', 3, 15, 2)""")
            c.execute("""insert into items values(Null, 'Dress1', 10, 10, 2)""")
            c.execute("""insert into items values(Null, 'T-Shirt1', 22, 15, 1)""")
            c.execute("""insert into items values(Null, 'Jacket1', 20, 25, 1)""")
            c.execute("""insert into items values(Null, 'Shoes', 50, 50, 1)""")
            c.execute(
                """insert into users values(1, 'mfuentes', 'control123', 'mfuentes@test.com', 'Magali', 'Fuentes')""")

            conn.commit()

            # c.execute("""select * from categories """)
            #
            # for row in c:
            #     print(row)
            #
            # c.close()
        return conn

    """Method to insert Item"""

    def insert_item(self, description, price, stock, categoryId):
        # item = (itemid, description, price, stock, categoryId)
        query = "INSERT INTO items VALUES (?,?, ?, ?, ?);"

        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        # cursor.execute(query, list(item))
        cursor.execute(query, (None, description, price, stock, categoryId))
        cursor.close()
        connection.commit()
        connection.close()

    """Method to insert Category"""
    def insert_category(self, categoryid, name):
        query = "INSERT INTO categories VALUES (?, ?);"
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(query, (categoryid, name))
        cursor.close()
        connection.commit()
        connection.close()

    """Method to insert user"""

    def insert_user(self, id, username, password, email, firstname, lastname):
        query = "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?);"
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(query, (id, username, password, email, firstname, lastname))
        cursor.close()
        connection.commit()
        connection.close()

    """Method that will be used when user wants to checkout """

    def insert_cart(self, userid, itemid):
        query = "INSERT INTO categories VALUES (?, ?);"
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(query, (userid, itemid))
        cursor.close()
        connection.commit()
        connection.close()

    """Mehtod that will show all categories"""
    def select_category(self, categoryid):
        query = "select categoryId, name from categories where categoryid = ?;"
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(query, categoryid)
        data = cursor.fetchall()
        for row in data:
            print(row)

        cursor.close()
        connection.commit()
        connection.close()

    """Mehtod that will show all data from specific table"""
    def select_table(self, table):
        query = "select * from " + table
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        for row in data:
            print(row)

        cursor.close()
        connection.commit()
        connection.close()

    """Method that can be used to update the quantity that we have in stock of the selected product afert a checkout is done"""
    def updateItem(self, stock, itemid):
        newstock = stock -1
        query = "update items set stock = " + str(newstock) + " where itemid = ?;"
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(query, itemid)

        cursor.close()
        connection.commit()
        connection.close()

    """Method that can be used to delete a item"""
    def deleteItem(self, itemid):
        query = " delete from items where itemid = ?;"
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(query, itemid)
        cursor.close()
        connection.commit()
        connection.close()



c = ConnectionDB()
c.getConnection()

"""Examples how the methods work """
# c.select_category(str(1))
# c.select_table("items")
# c.updateItem(25,str(4))
# c.deleteItem(str(3))