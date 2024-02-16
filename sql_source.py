import pymysql
#from sqlalchemy import create_engine
import pandas as pd

def sql_create_connection(data_b):
    global mydb
    mydb = pymysql.connect(host = 'localhost', user = 'root', password = 'yoga1234$', database=data_b)
    return mydb

    
def sql_create_database(database):
    mydb = pymysql.connect(host = 'localhost', user = 'root', password = 'yoga1234$')
    cursor = mydb.cursor()
    cursor.execute(f"CREATE DATABASE if not exists {database}")
    cursor.execute(f'USE {database}')
    
def sql_create_table(table):
    mycursor = mydb.cursor()

    mycursor.execute(f"CREATE TABLE if not exists {table} (name VARCHAR(50), \
                                            job VARCHAR(50), \
                                            mail VARCHAR(50), \
                                            web VARCHAR(50), \
                                            num1 TEXT(50), \
                                            num2 TEXT(50), \
                                            address_1 VARCHAR(50),\
                                            address_2 VARCHAR(50), \
                                            address_3 VARCHAR(50), \
                                            address_4 VARCHAR(50), \
                                            person_id int PRIMARY KEY AUTO_INCREMENT)")
        
    

def sql_insert(table, dic):
    mycursor = mydb.cursor()
    mycursor.execute(f"INSERT INTO {table} (name, job, mail, web, num1, num2, address_1, address_2, address_3, address_4) \
                                                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"\
                                                 ,(dic.get("name"),dic.get("job"),dic.get("mail"),dic.get("web"),dic.get("num1")\
                                                     ,dic.get("num2"),dic.get("address_1"),dic.get("address_2"),dic.get("address_3"),dic.get("address_4")))
    mydb.commit()

    print(mycursor.rowcount,"added successfully")


def sql_modify_table(table, coloum, value, id):
    mycursor = mydb.cursor() 
    mycursor.execute(f"UPDATE {table} SET {coloum}='{value}' where person_id={id}")
    mydb.commit()

def sql_get_columns(table):
    mycurser = mydb.cursor()
    mycurser.execute(f"SHOW COLUMNS FROM {table}")
    output = mycurser.fetchall()
    list = []
    for x in output:
        list.append(x[0])
    return list

def sql_colums_value(table , coloum):
    mycurser = mydb.cursor()
    mycurser.execute(f"SELECT {coloum} FROM {table}")
    output = mycurser.fetchall()
    list = []
    for x in output:
        list.append(x[0])
    return list

def sql_prime_number(table, coloum, value, id):
    mycurser = mydb.cursor()
    mycurser.execute(f"SELECT {id} FROM {table} WHERE {coloum}='{value}'")
    output = mycurser.fetchall()
    list = []
    for x in output:
        list.append(x[0])
    return list

def sql_get_detail_prime_num(table, num , id):
    mycurser = mydb.cursor()
    mycurser.execute(f"SELECT * FROM {table} WHERE {id}={num}")
    output = mycurser.fetchall()
    list = []
    for x in output[0]:
        list.append(x)
    return list