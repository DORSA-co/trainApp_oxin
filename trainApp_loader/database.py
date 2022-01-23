

import re
import mysql.connector
from mysql.connector import Error
def check_connection():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='oxin_images',
                                            user='root',
                                            password='Dorsa1400@')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchall()
            print("You're connected to database: ", record)
            return True

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        print("MySQL connection is closed")


def add_data(data):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='oxin_images',
                                            user='root',
                                             password='Dorsa1400@')

        mySql_insert_query = """INSERT INTO images (id,heat,psn,pdln,lenght) 
                            VALUES 
                            (%s,%s, %s, %s,%s) """
        

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, data)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into images table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into images table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
def report_last(tedad):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='oxin_images',
                                            user='root',
                                             password='Dorsa1400@')

        sql_select_Query = "select * from images ORDER BY id DESC LIMIT {}".format(tedad)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        # print(records)
        # print(len(records))
    #    print("\nPrinting each row")
        # for row in records:
        #     print("Id = ", row[0], )
        #     print("Name = ", row[1])
        #     print("Price  = ", row[2])
        #     print("Purchase date  = ", row[3], "\n")


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
    return records
def search_id(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='oxin_images',
                                            user='root',
                                             password='Dorsa1400@')

        sql_select_Query = "SELECT * FROM images WHERE ID = {}".format(id)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        print(records)
        print(len(records))
    #    print("\nPrinting each row")
        # for row in records:
        #     print("Id = ", row[0], )
        #     print("Name = ", row[1])
        #     print("Price  = ", row[2])
        #     print("Purchase date  = ", row[3], "\n")


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
    return records

def delete():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='oxin_images',
                                            user='root',
                                             password='Dorsa1400@')
        sql_select_Query = "DELETE FROM  oxin_images.images;"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)        
        print('delete')                                   
    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
check_connection()
# #X=search_id(3)
data=('017',21,21,122,50.8)
add_data(data)

# delete()

# report_last(1)