'''
Created on Feb 20, 2020

@author: rodri
'''
import sqlite3
from sqlite3 import Error
class SQLite3DB:
    
    #TODO make queries not string concats
    def __init__(self, db_file, FIELD_SIZE, NUM_FIELDS):
        self._db_file = db_file
        self.__FIELD_SIZE = FIELD_SIZE
        self.__NUM_FIELDS = NUM_FIELDS
        self.__ID_SIZE = FIELD_SIZE
        self.__MAX_ROWS = 2
        try:
            self._conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        self._conn.row_factory = sqlite3.Row

    def get_connection(self):
        return self._conn

    def set_id_size(self, ID_SIZE):
        self.__ID_SIZE = ID_SIZE
    
    def set_max_rows(self, MAX_ROWS):
        self.__MAX_ROWS = MAX_ROWS

    def create_table(self, create_table_sql):
        try:
            cur = self._conn.cursor()
            cur.execute(create_table_sql)
        except Error as e:
            print(e)

    def create_task(self, task, table_name):
        """
        Create a new task
        :param conn:
        :param task:
        :return:
        """
        sql = "INSERT INTO " + table_name + "(name,priority,status_id,due_date) VALUES(?,?,?,?)"
        cur = self._conn.cursor()
        cur.execute(sql, task)
        return cur.lastrowid

    def update_task(self, table_name, update_field, updated_val, task_id):
        sql = "UPDATE " + table_name + " SET " + str(update_field) + " = " + str(updated_val) + " WHERE id = " + task_id + ";"
        cur = self._conn.cursor()
        cur.execute(sql)

    def sort_tasks(self, table_name, sort_field, direction):
        sql = "SELECT * FROM " + table_name + " ORDER BY " + sort_field + " " + direction + ";"
        cur = self._conn.cursor()
        cur.execute(sql)
        return cur

    def delete_task(self, task_id, table_name):
        self._conn.execute("DELETE FROM "+ table_name + " WHERE id=" + str(task_id))

    def select_task(self, task_id, table_name):
        cur = self._conn.execute("SELECT * FROM " + table_name + " WHERE id=" + str(task_id))
        task = cur.fetchone()
        #task = task[1:]
        return task
    
    def refresh_table(self, table_name):
        cur = self._conn.execute("SELECT id FROM " + table_name)
        for task_id_tup in cur.fetchall():
            for task_id in task_id_tup:
                curr_task = self.select_task(task_id, table_name)
                self.delete_task(task_id, table_name)
                self.create_task(curr_task[1:], table_name)
    

    def clear_table(self, table_name):
        self._conn.execute("DELETE FROM " + table_name + ";")
        
    def expand_row(self, task_id, table_name):
        task = self.select_task(task_id, table_name)
        headers = self._conn.execute("PRAGMA table_info(tasks);")
        self.print_header(headers)
        row_to_print = ''
        for field in task:
            row_to_print += str(field) + ','
        print(self.format_string_to_table(row_to_print[:-1], True))
        self.print_row_separator()
        

    def print_table(self, table_name, rows=None):
        if rows == None:
            rows = self.fetch_table(table_name)
        headers = self._conn.execute("PRAGMA table_info(tasks);")
        self.print_header(headers)

        for row in rows:
            row_to_print = ''
            for field in row:
                row_to_print += str(field) + ','
            print(self.format_string_to_table(row_to_print[:-1]))
            self.print_row_separator()

    def fetch_table(self, table_name):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = self._conn.cursor()
        cur.execute("SELECT * FROM " + table_name)
     
        rows = cur.fetchall()
        return rows

    def print_header(self, headers):
        beginning = ' '
        beginning += '_' * self.__ID_SIZE
        s = ''
        s += '_' * self.__FIELD_SIZE * self.__NUM_FIELDS
        s += '_' * self.__NUM_FIELDS
        s = beginning + s
        print(s)
        
        row_to_print = ''
        for header in headers:
            row_to_print += str(header[1]) + ','
        print(self.format_string_to_table(row_to_print[:-1]))
        self.print_row_separator()

    def print_row_separator(self):
        beginning = "|"
        beginning += "_" * self.__ID_SIZE
        s = "_" * self.__FIELD_SIZE
        out = "|"
        out += s
        out = out * self.__NUM_FIELDS
        out += "|"
        out = beginning + out
        print(out)
    
    def table_formatting(self, list_to_fmt):
        num_rows = 1
        fmt_out = []
        i = 0
        while i < num_rows:
            fmt_row = []
            j = 0
            for member in list_to_fmt:
                if (i == 0):
                    size = 1
                    if len(member) > self.__FIELD_SIZE:
                        size = len(member) // self.__FIELD_SIZE
                        if (len(member) % self.__FIELD_SIZE != 0):
                            size += 1
                    if (size > num_rows):
                        num_rows = size
                fmt_row.append(member[:self.__FIELD_SIZE])
                #fmt_row[-1] += " " * (self.__FIELD_SIZE - len(fmt_row[-1]))
                member = member[self.__FIELD_SIZE:]
                list_to_fmt[j] = member
                j += 1
                    
            fmt_out.append(fmt_row)
            i += 1
            
        return fmt_out
                    
    
    def format_string_to_table(self, str_to_fmt, is_expanded = False):
        str_to_fmt = str_to_fmt.split(',')
        fmt_list = self.table_formatting(str_to_fmt)
        if (not is_expanded):
            fmt_list = self.compress_table(fmt_list)
        fmt_out = ""
        for row in fmt_list:
            fmt_out += '|'
            num_spaces = self.__ID_SIZE - len(row[0])
            fmt_out += " " * (num_spaces // 2)
            fmt_out += row[0]
            fmt_out += " " * (num_spaces // 2 + num_spaces % 2)
            fmt_out += "|"
            row = row[1:]
            for member in row:
                num_spaces = self.__FIELD_SIZE - len(member)
                fmt_str = " " * (num_spaces // 2)
                fmt_str += member
                fmt_str += " " * (num_spaces // 2 + num_spaces % 2)
                fmt_out += fmt_str + '|'
            fmt_out += "\n"
        return fmt_out[:-1]
    
    def compress_table(self,fmt_list):
        if (len(fmt_list) <= self.__MAX_ROWS):
            return fmt_list
        else:
            fmt_out = fmt_list[:self.__MAX_ROWS]
            fmt_row = fmt_out[-1]
            for i in range(len(fmt_row)):
                if (len(fmt_row[i]) >= self.__FIELD_SIZE - 3 and ' ' not in fmt_row[i][self.__FIELD_SIZE - 3:]):
                    fmt_out[-1][i] = fmt_out[-1][i][:self.__FIELD_SIZE - 3]
                    fmt_out[-1][i] += "..."
            return fmt_out
    
    def check_list_empty(self, l):
        for el in l:
            if el != "":
                return False
        return True