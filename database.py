

import re
from matplotlib.pyplot import flag
import mysql.connector
from mysql.connector import Error
from numpy import rec
# from tenacity import retry_if_exception


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
            #print('Q:', mySql_insert_query)                   
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

    def update_record(self,table_name,col_name,value,id_name,id_value):
        
        print('id_value',table_name,col_name,value,id_name,id_value)
        if self.check_connection:
            cursor,connection=self.connect()

            mySql_insert_query = """UPDATE {} 
                                    SET {} = {}
                                    WHERE {} ={} """.format(table_name,col_name,("'"+value+"'"),id_name,("'"+id_value+"'"))
            #print(mySql_insert_query)
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

            field_names = [col[0] for col in cursor.description]
            res = []

            connection.close()
            cursor.close()
            print("MySQL connection is closed")

            for record in records:
                    record_dict = {}
                    for i in range( len(field_names) ):
                        record_dict[ field_names[i] ] = record[i]
                    res.append( record_dict )

            return res


            return records


    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------

    def search(self,table_name,param_name, value,int_type=True):

        user_id=value
        try:
            if self.check_connection:
                cursor,connection=self.connect()

                if int_type:
                    sql_select_Query = "SELECT * FROM {} WHERE {} = {};".format(table_name,param_name,str(value))
                    cursor=self.execute_quary(sql_select_Query, cursor, connection)
                else:

                    sql_select_Query = """SELECT * FROM {} WHERE {} = {} """.format(table_name,param_name,("'"+str(value)+"'"))
                    cursor=self.execute_quary(sql_select_Query, cursor, connection)


                print('cursor',cursor)

                records = cursor.fetchall()
                print("Total number of rows in table: ", cursor.rowcount)
                #print(len(records),records)
                #----------------------------
                print('if',records)
                
                field_names = [col[0] for col in cursor.description]
                res = []
                for record in records:
                    # print('record',record)
                    record_dict = {}
                    for i in range( len(field_names) ):
                        record_dict[ field_names[i] ] = record[i]
                    # print('record_dict',record_dict)
                    
                    res.append( record_dict )
                # print('res',res)
                return res


            return res
        except:
            return [],[]

        # except:
        #     print('No record Found')
        #     return [],[]
    


        #     print('No record Found')
        #     return [],[]
    






    def search_with_range(self,table_name, col_names, values, limit=False, limit_range=[0,20], count=False):
        # SELECT * FROM saba_database.binary_models where (algo_name,accuracy) = (0,0) and epochs between 2 and 4 and split_ratio between 20 and 30 and batch_size between 1 and 8
        try:
            if self.check_connection:
                cursor,connection=self.connect()

                if count:
                    sql_select_Query = "SELECT count(*) FROM {} WHERE ".format(table_name)
                else:
                    sql_select_Query = "SELECT * FROM {} WHERE ".format(table_name)

                # single values
                single_cols_query = '('
                single_vals_query = '('
            
                for i, col in enumerate(col_names):
                    if len(values[i]) == 1:
                        if i != 0:
                            single_cols_query += ','
                            single_vals_query += ','
                        single_cols_query += col
                        single_vals_query += str(values[i][0])
                single_cols_query += ')'
                single_vals_query += ')'
            
                # add single query yo main query
                if not single_cols_query == '()' and not single_vals_query == '()':
                    sql_select_Query = sql_select_Query + single_cols_query + '=' + single_vals_query + ' '

                # range values
                for i, col in enumerate(col_names):
                    if len(values[i]) > 1:
                        if i != 0:
                            sql_select_Query += "AND "
                        #
                        sql_select_Query += "{} BETWEEN {} AND {} ".format(col, str(values[i][0]), str(values[i][1]))
                

                if limit:
                    sql_select_Query += "LIMIT {},{}".format(limit_range[0], limit_range[1])


                #print(sql_select_Query)

                cursor=self.execute_quary(sql_select_Query, cursor, connection)

                records = cursor.fetchall()
                #print("Total number of rows in table: ", cursor.rowcount)
                #print(len(records),records)
                #----------------------------
                # print(records)
                
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

    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def get_all_content(self,table_name, count=False, limit=False, limit_range=[0,20]):

        try:
            if self.check_connection:
                cursor,connection=self.connect()

                if count:
                    sql_select_Query = "select count(*) from {}".format(table_name)
                else:
                    if not limit:
                        sql_select_Query = "select * from {}".format(table_name)
                    else:
                        sql_select_Query = "select * from {} LIMIT {},{}".format(table_name, limit_range[0], limit_range[1])
                    
                cursor=self.execute_quary(sql_select_Query, cursor, connection)
                # cursor.execute(sql_select_Query)
                records = cursor.fetchall()
                print("Total number of rows in table: ", cursor.rowcount)
                #print(records)

                field_names = [col[0] for col in cursor.description]

                connection.close()
                cursor.close()
                print("MySQL connection is closed")

                res = []
                for record in records:
                        record_dict = {}
                        for i in range( len(field_names) ):
                            record_dict[ field_names[i] ] = record[i]
                        res.append( record_dict )

                return res
            else:
                return []

            # return records
            return []

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
            return []

    def check_table_exist(self,table_name):

        try:
            if self.check_connection:
                cursor,connection=self.connect()
            sql_check_table = "SELECT * FROM {}.{};".format(self.data_base_name,table_name)
            cursor=self.execute_quary(sql_check_table, cursor, connection)       
            # print('check')    
            return 'Exist'                              
        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)


if __name__ == "__main__":
    db=dataBase('root','root','localhost','saba_database')

    # db.get_col_name('996','camera_settings','id')

    # data=(0,)*10
    # data=(0,0,0,0,1920,1200,0,0,0,0,0)

    # x=db.get_all_content('defects_info')
    # print(x)

    record = db.search( 'users' , 'user_name', 'testt')[0]
    print(record)
    # table_name,parametrs,len_parameters)

    # db.add_record(data,'coils_info','(id,coil_number,heat_number,ps_number,pdl_number,lenght,width,operator,time,date,main_path)',11)
    # db.add_record(data,'camera_settings','(gain_top,gain_bottom,expo_top,expo_bottom,width,height,offset_x,offset_y,interpacket_delay,packet_size,id)',11)
 
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