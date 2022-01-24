# from trainApp_loader import database
import sqlite3
from sqlite3 import Error
def add_remove_label(text):
    cont=0
    create_connection('settings.db')
    conn = sqlite3.connect('settings.db')
    conn = sqlite3.connect('settings.db')
    cur = conn.cursor()       
    cur.execute('select * from labels')
    rec = cur.fetchall()
    conn.commit()
    conn.close()
    for i in range (len(rec) ):
        if str(text)==(str(rec[i][0])):
            print('remove')
            deleteSqliteRecord(text)
            cont=1
    if cont==0:
        print('add')
        insertVaribleIntoTable(text)
            
        return str(rec[0][0])


def deleteSqliteRecord(id):
    try:
        sqliteConnection = sqlite3.connect('settings.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """DELETE from labels where name = ?"""
        cursor.execute(sql_update_query, (id,))
        sqliteConnection.commit()
        print("Record deleted successfully")
        # cursor.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")


# def add(i):

def insertVaribleIntoTable(id):
    try:
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()
        print("Connected to SQLite")
        mySql_insert_query = """        INSERT INTO labels (name)
        VALUES (?); """

        # cursor = connection.cursor()
        cur.execute(mySql_insert_query, (id,))
        conn.commit()
        conn.close()
        # cur.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)

    finally:
        if conn:
            conn.close()
            # cur.close()
            print("The SQLite connection is closed")


# insertVaribleIntoTable('test')



#     conn = sqlite3.connect('settings.db')
# cur = conn.cursor()
# sql = "UPDATE language SET lan = '{}' WHERE id = 0".format(text)
# cur.execute(sql) 
  
# x=['Arial', 'Arial Black', 'Forte', 'Gigi', 'jokerman' ,'Times New Roman' , 'Zilla Slab']
# self.comboBox_font.addItems(x)
# conn = sqlite3.connect('settings.db')
# cur = conn.cursor()       
# cur.execute('select * from names')
# rec = cur.fetchall()
# conn.commit()
# conn.close()    

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('ok')
        return conn
    except Error as e:
        print(e)
        # eror_window(msg=' NO connection to database {}'.format(db_file),level=3)



# insertVaribleIntoTable('milad')
# add_remove_label('milad')



def catch_labels():
    try:
        cont=0
        # create_connection('settings.db')
        conn = sqlite3.connect('settings.db')
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from labels')
        rec = cur.fetchall()
        conn.commit()
        conn.close()
        labels=[]
        for i in range (len(rec) ):
            labels.append(str(rec[i][0]))
    
    except:
        print('eror')
    return labels