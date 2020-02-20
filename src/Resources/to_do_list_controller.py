'''
Created on Feb 20, 2020

@author: rodri
'''
from Resources.sqlite3_db import *
import os

def sort_table(db, direction="ASC"):
    sort_field = input("BY:\n ... ")
    try:
        cur = db.sort_tasks("tasks", sort_field, direction)
    except Error as e:
        print("Invalid field")
        #print(e)
        sort_table(db, direction)
    rows = cur.fetchall()
    os.system("cls")
    print("Your to-do list organized by " + sort_field)
    db.print_table("tasks", rows)
    input()

def add_task(db):
    task = input(" ... ")
    task_list = task.strip("()").split(',')
    task_tup = tuple(task_list)
    try:
        db.create_task(task_tup, "tasks")
    except Error as e:
        print("Invalid task")
        add_task(db)

def update_table(db):
    task_id = input("Enter task id to update:\n ... ")
    updated_val = input("Enter updated value:\n ... ")
    updated_val = "'" + updated_val + "'"
    try:
        db.update_task("tasks", "status_id", updated_val, task_id)
    except Error as e:
        print("Invalid info")
        #print(e)
        update_table(db)

def edit_table(db):
    user_in = input("Enter task id and field to update as follows: id#,field\n ... ")
    user_in = user_in.split(',')
    task_id = user_in[0]
    update_field = user_in[1]

    updated_val = input("Enter updated value:\n ... ")
    updated_val = "'" + updated_val + "'"
    try:
        db.update_task("tasks", update_field, updated_val, task_id)
    except Error as e:
        print("Invalid info")
        #print(e)
        update_table(db)

def see_table(db, table_name=None):

    if table_name == None:
        table_name = input(" ... ")
        
    os.system("cls")
    print(table_name)
        
    try:
        db.print_table(table_name)
    except Error as e:
        print("Invalid table")
        see_table(db, table_name)
    input()

def finish_task(db):
    #does not handle having a todo item in tasks with same name as one in task_history
    task_id = input(" ... ")
    task = db.select_task(task_id, "tasks")
    try:
        db.create_task(tuple(task), "task_history")
    except Error as e:
        '''print("Invalid task")
        print(tuple(task))
        print(e)'''
    try:
        db.delete_task(task_id, "tasks")
    except Error as e:
        print("Invalid task")
        finish_task(db)
        #print(tuple(task))
        #print(e)
    return

def delete_task(db):
    task_id = input(" ... ")
    try:
        db.delete_task(task_id, "tasks")
    except Error as e:
        print("Invalid task id")
        delete_task(db)

def guard_input_y_or_n(message):
    y_or_n = input(message + " (y/n)?\n ... ")
    while(y_or_n.lower() != "n" and y_or_n.lower() != "y"):
        y_or_n = input(message + " (y/n)?\n ... ")
    return y_or_n

def clear_table(db, table_name="tasks"):
    y_or_n = guard_input_y_or_n("Are you sure you want to clear " + table_name).lower()
    if (y_or_n == "y"):
        db.clear_table(table_name)

