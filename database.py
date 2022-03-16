

import re
from matplotlib.pyplot import flag
import mysql.connector
from mysql.connector import Error
from numpy import rec


TABELS_NAME = {'coils_info':'images',
               }
               

class dataBase:
    def __init__(self,username,password,host,database_name):
        pass
        self.user_name=username
        self.password=password
        self.host=host
        self.data_base_name=database_name
        self.check_connection()
        
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    def connect(self):
            connection = mysql.connector.connect(host=self.host,
                                                database=self.data_base_name,
                                                user=self.user_name,
                                                password=self.password)  
            cursor = connection.cursor()

            return cursor,connection     

    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    def check_connection(self):
        flag=False
        try: 
            cursor,connection=self.connect()
            flag=True
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
            return False
        finally:
            if flag and connection.is_connected():
                cursor.close()
                connection.close()
            print("MySQL connection is closed")

    
    def execute_quary(self,quary, cursor, connection,need_data=False, close=False):
        
        try:
            if need_data:
                cursor.execute(quary,data)

            else:
                cursor.execute(quary)

            # connection.commit()
            if close:
                cursor.close()
            else:
                return cursor
        except Error as e:
            print("Error while connecting to MySQL", e)
        


    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    def add_record(self,data,table_name,parametrs,len_parameters):

        s ='%s,'*len_parameters
        s = s[:-1]
        s = '(' + s + ')'
        

        if self.check_connection:
            cursor,connection=self.connect()

            mySql_insert_query = """INSERT INTO {} {} 
                                VALUES 
                                {} """.format(table_name,parametrs,s)
            cursor.execute(mySql_insert_query,data)
            # mySql_insert_query=(mySql_insert_query,data)
            # self.execute_quary(mySql_insert_query, cursor, connection, close=False,need_data=True )
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into images table")
            cursor.close()
            return True

        else:
            return False


    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------

    def update_record(self,table_name,col_name,value,id,id_value):
        

        if self.check_connection:
            cursor,connection=self.connect()

            mySql_insert_query = """UPDATE {} 
                                    SET {} = {}
                                    WHERE {} ={} """.format(table_name,col_name,("'"+value+"'"),id,id_value)
            print(mySql_insert_query)
            cursor.execute(mySql_insert_query)
            # mySql_insert_query=(mySql_insert_query,data)
            # self.execute_quary(mySql_insert_query, cursor, connection, close=False,need_data=True )
            connection.commit()
            print(cursor.rowcount, "Record Updated successfully ")
            cursor.close()
            return True

        else:
            return False



    def remove_record(self, id, table_name):
        if self.check_connection:
            cursor,connection=self.connect()

            mySql_delete_query = """DELETE FROM {} WHERE width={}""".format(table_name, id)

            self.execute_quary(mySql_delete_query, cursor, connection, False )
            connection.commit()
            print(cursor.rowcount, "Remove successfully from table {}".format(table_name))
            cursor.close()
            return True


    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    def report_last(self,table_name,parametr,count):
        if self.check_connection:
            cursor,connection=self.connect()

            sql_select_Query = "select * from {} ORDER BY {} DESC LIMIT {}".format(table_name,parametr,count)
            cursor=self.execute_quary(sql_select_Query, cursor, connection)
            # cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            print("Total number of rows in table: ", cursor.rowcount)
            print(records)
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

            field_names = [col[0] for col in cursor.description]
            res = []
            for record in records:
                    record_dict = {}
                    for i in range( len(field_names) ):
                        record_dict[ field_names[i] ] = record[i]
                    res.append( record_dict )

            return res


            return records


    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------

    def search(self,table_name,param_name, value):
        try:
            if self.check_connection:
                cursor,connection=self.connect()

                sql_select_Query = "SELECT * FROM {} WHERE {} = {}".format(table_name,param_name,value)
                cursor=self.execute_quary(sql_select_Query, cursor, connection)

                records = cursor.fetchall()
                #print("Total number of rows in table: ", cursor.rowcount)
                #print(len(records),records)
                #----------------------------
                
                field_names = [col[0] for col in cursor.description]
                res = []
                for record in records:
                    record_dict = {}
                    for i in range( len(field_names) ):
                        record_dict[ field_names[i] ] = record[i]
                    res.append( record_dict )

                return res
            return [],[]

        except:
            print('No record Found')
            return [],[]


    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------

    def delete(self,db_name,table_name):
        try:
            if self.check_connection:
                cursor,connection=self.connect()
            sql_Delete_table = "DELETE FROM  {}.{};".format(db_name,table_name)
            cursor=self.execute_quary(sql_Delete_table, cursor, connection)       
            print('delete')                                   
        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)


    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------

    def get_col_name(self,table_name,param_name, value):
        if self.check_connection:
            cursor,connection=self.connect()
            

            cursor = connection.cursor()
            cursor.execute("select database();")

            field_names = [col[0] for col in cursor.description]

            print(field_names)

        return field_names


if __name__ == "__main__":
    db=dataBase('root','Dorsa1400@','localhost','saba_database')

    # db.get_col_name('996','camera_settings','id')

    # data=(0,)*10
    data=(0,0,0,0,1920,1200,0,0,0,0,0)

    

    # table_name,parametrs,len_parameters)

    # db.add_record(data,'coils_info','(id,coil_number,heat_number,ps_number,pdl_number,lenght,width,operator,time,date,main_path)',11)
    db.add_record(data,'camera_settings','(gain_top,gain_bottom,expo_top,expo_bottom,width,height,offset_x,offset_y,interpacket_delay,packet_size,id)',11)
 
    #db.add_record(data,'coils_info','(id,coil_number,heat_number,ps_number,pdl_number,lenght,width,operator,time,date,main_path)',11)

    #db.report_last('coils_info','id',30)

    # db.remove_record('1920', 'camera_settings')

    # db.report_last('coils_info','id',30) 

    # db.search('996','coils_info','id')



# report_last(self,table_name,parametr,count)



# CREATE SCHEMA `saba_database` ;


# CREATE TABLE `saba_database`.`coils_info` (
#   `id` INT NOT NULL,
#   `coil_number` VARCHAR(45) NOT NULL,
#   `heat_number` VARCHAR(45) NULL,
#   `ps_number` VARCHAR(45) NULL,
#   `pdl_number` VARCHAR(45) NULL,
#   `lenght` VARCHAR(45) NULL,
#   `width` VARCHAR(45) NULL,
#   `operator` VARCHAR(45) NULL,
#   `time` VARCHAR(45) NULL,
#   `date` VARCHAR(45) NULL,
#   PRIMARY KEY (`id`));