import os
import sqlite3


class ConnectionDB:
    dbName = "shoppingCart.db"

    def __init__(self):
        self.__exist = os.path.exists(self.dbName)


    def getConnection(self):
        conn = sqlite3.connect(self.dbName)
        c = conn.cursor()
        if not self.__exist:

            c.execute("CREATE TABLE IF NOT EXISTS PRODUCT(product_id integer ,product_name varchar(100)  not null, description varchar(200) not null , price real not null , stock integer not null , category_id integer not null , primary key(product_id),foreign key(category_id) references category(category_id));")
            c.execute("CREATE TABLE IF NOT EXISTS CATEGORY(category_id integer , category_name varchar(200) not null, primary key(category_id));")
            c.execute("CREATE TABLE IF NOT EXISTS USER(user_id integer, user_name varchar(100) not null, password varchar(100) not null,email varchar(100) not null, firstname varchar(100) not null, lastname varchar(100) not null, phonenumber integer,type_user varchar(20), state_user varchar(20), primary key(user_id));")
            c.execute("CREATE TABLE IF NOT EXISTS PURCHASE(billing_id varchar(100), user_id integer not null,product_id integer not null,quantity integer not null,price real not null, foreign key(user_id) references user(user_id),foreign key(product_id) references product(product_id));")


        return conn






