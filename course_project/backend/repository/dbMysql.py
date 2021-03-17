import mysql.connector
from mysql.connector import errorcode
import traceback
import logging


class Database:
    '''
    Database class is responsible for talking to Mysql database of the course managament system and perform
    CRUD(Create, Read, Update, Delete) functionalities.
    '''
    def __init__(self):
        self._config = {
            'user': 'root',
            'password': 'Mysqlpassword',
            'host': '127.0.0.1',
            'database': 'course_mngm',
            'auth_plugin':'mysql_native_password',
            'raise_on_warnings': True
            }
        self.tables = {
            "courses":"courses",
            "sections":"sections",
            "buildings":"buildings"
        }

    def execute(self, query, args):
        conn = mysql.connector.connect(**self._config)
        cursor = conn.cursor()
       
        try:
            if args:
                cursor.execute(query, args)
                print(query)
            else: 
                cursor.execute(query)
            affected_rows = cursor.rowcount
            results = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]
            cursor.execute('COMMIT')
            return (affected_rows, results, field_names)
        except Exception:
            logging.error(traceback.format_exc())
        finally:
            cursor.close()
            conn.close()
        return None

    def mk_in_str(self, length):
        '''
        Make a comma-separated string of length question marks
        '''
        return ", ".join(["%s"] * length)

    def create(self, data, table):
        '''
        Insert a row into a table
        Input:
            data(dict): values to be inserted (lst)
            table(string): the intended name of the table
        Output:
            success(boolean): Whether the insertion was successful
        '''
        
        success = False
        table_name = self.tables[table]
        place_holders = self.mk_in_str(len(data))
        col_names = ", ".join(list(data.keys()))
        query = "INSERT INTO "+table_name+" ("+col_names+") VALUES ("+place_holders+")"
        args = list(data.values())
        rv = self.execute(query, args)
        if rv:
            affected_rows, results, field_names = rv
            if affected_rows > 0:
                success =  True
        return success
    
    def find(self, select, from_tables, criteria=None, limit=None):
        '''
        Input:
        select: list
        table: dictionary{"tables":[], "ons":[]}
        criteria: dict {"col": value}

        '''
        results=None
        where_query=None
        args = []
        #build the select part
        select =  ",".join(select)
        #build the from part
        from_query = self.build_join(from_tables)
        query = "SELECT "+select+" FROM "+from_query
        if criteria:
            where_query, args_list = self.build_where(criteria)
            query = query+" WHERE "+where_query
            args = args_list
        if limit:
            query = query+" "+" ".join(limit)
        rv = self.execute(query, args)
        if rv:
            affected_rows, results, field_names = rv
        return results, field_names

    def delete(self, criteria, table):
        '''
        Delete one row from one of the table
        Inputs:
            criteria(dict): dictionary storing conditions ({"col": value})
            table(string): target table 
        Output:
            
        '''
        success = False
        table_name = self.tables[table]
        where_query, args_list = self.build_where(criteria)
        query = "DELETE FROM "+table_name+" WHERE "+where_query
        rv = self.execute(query, args_list)
        if rv:
            affected_rows, results, field_names = rv
        if affected_rows > 0:
            success =  True
        return success
        
    def update(self, new_data, criteria, table):
        '''
        Inputs:
            new_data(dict)
            criteria(dict)
            table(str)
        '''
        success = False
        args_list=[]
        table_name = self.tables[table]
        new_cols_values = ", ".join([x+"=%s" for x in list(new_data.keys())])
        args_list.extend(new_data.values())
        where_query, args_list_where = self.build_where(criteria)
        args_list.extend(args_list_where.values())
        query = f"UPDATE {table_name} SET {new_cols_values} WHERE {where_query}"
        rv = self.execute(query, args_list)
        if rv:
            affected_rows, results, field_names = rv
        if affected_rows > 0:
            success =  True
        return success

    def build_join(self, tables):
        if tables["ons"]:
            join_str = "{} ON {}".format(" JOIN ".join(tables["tables"]), " AND ".join(tables["ons"]))
        else:
            join_str = " JOIN ".join(tables["tables"])
        return join_str

    def build_where(self, criteria):
        '''
        Build the "where" part of the sql statement
        Inputs:
            criteria(dict)
        '''
        criteria_list = []
        args_list = []
        for key, value in criteria.items():
            if type(value) == list:
                if len(value) > 1:
                    query = key+" in ("+self.mk_in_str(len(value))+")"
                else:
                    query = key+"= %s"
                args_list.extend(value)
            elif type(value) == dict:
                operator = value["operator"]
                query = f"{key} {operator} %s"
                args_list.append(value["arg"])
            else:
                query = key+"= %s"
                args_list.append(value)
            criteria_list.append(query)
        where_query = " AND ".join(criteria_list)
        return (where_query, args_list)
            
    