'''
Created on Feb 20, 2020

@author: rodri
'''
#import sqlite3
import sys
#import os
from Resources.to_do_list_controller import *
from Resources.sqlite3_db import *
from Resources.to_do_help import *
#from sqlite3 import Error

FIELD_SIZE = 15
NUM_FIELDS = 4
ID_SIZE = 5

def menu(conn, db):
    while(True):
        print("Welcome to your to-do list. Here are the tasks you have to do:")
        db.print_table('tasks')
        print()
        input_commands(conn, db)

def input_commands(conn, db):
    in_string = input(">>> ")
    in_string = in_string.upper()
    if in_string == "ADD" or in_string == "A":
        add_task(db)
    elif in_string == "DELETE" or in_string  == "D":
        delete_task(db)
    elif in_string == "FINISH" or in_string == "F":
        finish_task(db)
    elif in_string == "SEE":
        see_table(db)
        return
    elif in_string == "SEEHIST" or in_string == "SEEH":
        see_table(db, "task_history")
        return
    elif in_string == "EDIT" or in_string == "E":
        edit_table(db)
    elif in_string == "UPDATE" or in_string == "U":
        update_table(db)
    elif in_string == "SORT" or in_string == "S":
        sort_table(db)
        return
    elif in_string == "SORTDESC" or in_string == "SD":
        sort_table(db, "DESC")
        return
    elif in_string == "CLEAR" or in_string == "C":
        clear_table(db)
    elif in_string == "CLEARHIST" or in_string == "CH":
        clear_table(db, "task_history")
    elif in_string == "HELP" or in_string == "H":
        help_page_1()
    elif in_string == "HELP ADD":
        help_add()
    elif in_string == "HELP DELETE":
        help_delete()
    elif in_string == "HELP FINISH":
        help_finish()
    elif in_string == "HELP SEE":
        help_see()
    elif in_string == "HELP SEEHIST":
        help_see_hist()
    elif in_string == "HELP EDIT":
        help_edit()
    elif in_string == "HELP UPDATE":
        help_update()
    elif in_string == "HELP SORT":
        help_sort()
    elif in_string == "HELP SORTDESC":
        help_sort_desc()
    elif in_string == "HELP CLEAR":
        help_clear()
    elif in_string == "HELP CLEARHIST":
        help_clear_hist()
    elif in_string == "HELP EXIT":
        help_exit()
    elif in_string == "HELP HELP":
        help_help()
    elif in_string == "HELP 1":
        help_page_1()
    elif in_string == "HELP 2":
        help_page_2()
    elif in_string == "HELP 3":
        help_page_3()
    elif in_string == "EXIT" or in_string == "X":
        conn.commit()
        sys.exit(0)
    else:
        input_commands(conn, db)
    conn.commit()
    os.system("cls")

def main():
    database = 'C:/Users/rodri/Databases/to_do.db'

    sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer,
                                        status_id integer NOT NULL,
                                        due_date text,
                                        UNIQUE(name)
                                    ); """
    sql_create_task_history_table = """ CREATE TABLE IF NOT EXISTS task_history (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer,
                                        status_id integer NOT NULL,
                                        due_date text,
                                        UNIQUE(name)
                                    ); """
    
    db = SQLite3DB(database, FIELD_SIZE, NUM_FIELDS)
    conn = db.get_connection()
    db.set_id_size(ID_SIZE)

    if conn is not None:
        db.create_table(sql_create_tasks_table)
        db.create_table(sql_create_task_history_table)
    else:
        print("Error! cannot create the database connection.")
        
    menu(conn, db)
    conn.commit()
        
main()
