'''
Created on Feb 20, 2020

@author: rodri
'''
import os
ROW_LENGTH = 70

def help_page_1():
    os.system("cls")
    print("Help page 1 of 3:")
    print_separator()
    
    help_add_basic()
    print_separator()
    
    help_delete_basic
    print_separator()

    help_finish_basic()
    print_separator()

    help_see_basic()
    print_separator()
    
    help_see_hist_basic()
    print()
    ans = input("Enter a page number to go to that page, press enter to go to next page, or enter x to exit\n")
    while (ans != "" and ans != "\n" and ans != "x" and ans != "X" and ans != "1" and ans != "2" and ans != "3"):
        ans = input()
    ans = str(ans)

    if ans == "1":
        help_page_1()
    elif ans == "2" or ans == "\n" or ans == "":
        help_page_2()
    elif ans == "3":
        help_page_3()
    elif ans == "x" or ans == "X":
        return
    return
    
def help_page_2():
    os.system("cls")
    print("Help page 2 of 3:")
    print_separator()

    help_edit_basic()
    print_separator()

    help_update_basic()
    print_separator()

    help_sort_basic()
    print_separator()

    help_sort_desc_basic()
    print()
    ans = input("Enter a page number to go to that page, press enter to go to next page, or enter x to exit\n")
    while (ans != "" and ans != "\n" and ans != "x" and ans != "X" and ans != "1" and ans != "2" and ans != "3"):
        ans = input()
    ans = str(ans)

    if ans == "1":
        help_page_1()
    elif ans == "2":
        help_page_2()
    elif ans == "3" or ans == "\n" or ans == "":
        help_page_3()
    elif ans == "x" or ans == "X":
        return
    return

def help_page_3():
    os.system("cls")
    print("Help page 3 of 3:")
    print_separator()

    help_clear_basic()
    print_separator()

    help_clear_hist_basic()
    print_separator()

    help_exit_basic()
    print_separator()

    help_help_basic()
    print()
    ans = input("Enter a page number to go to that page, press enter or x to exit\n")
    while (ans != "" and ans != "\n" and ans != "x" and ans != "X" and ans != "1" and ans != "2" and ans != "3"):
        ans = input()
    ans = str(ans)

    if ans == "1":
        help_page_1()
    elif ans == "2":
        help_page_2()
    elif ans == "3":
        help_page_3()
    elif ans == "x" or ans == "X"  or ans == "\n" or ans == "":
        return
    return

def help_add():
    os.system("cls")
    help_add_basic()
    input()

def help_add_basic():
    print("ADD: Adds a task to the tasks table")
    print("Usage:")
    print(">>> ADD")
    print(" ... task_name,priority,status,due_date(optional)")

def help_delete():
    os.system("cls")
    help_delete_basic()
    input()

def help_delete_basic():
    print("DELETE: Delete a task in the tasks table")
    print("Usage:")
    print(">>> DELETE")
    print(" ... task_id")

def help_finish():
    os.system("cls")
    help_finish_basic()
    input()

def help_finish_basic():
    print("FINISH: 'Finishes' a task by moving the task to task_history")
    print("Usage:")
    print(">>> FINISH")
    print(" ... task_id")

def help_see():
    os.system("cls")
    help_see_basic()
    input()

def help_see_basic():
    print("SEE: Accesses and displays the given table")
    print("Usage:")
    print(">>> SEE")
    print(" ... table_name")

def help_see_hist():
    os.system("cls")
    help_see_hist_basic()
    input()

def help_see_hist_basic():
    print("SEEHIST: Accesses and displays the task_history table")
    print("Usage:")
    print(">>> SEEHIST")

def help_edit():
    os.system("cls")
    help_edit_basic()
    input()

def help_edit_basic():
    print("EDIT: Allows user to edit a value in the tasks table")
    print("Usage:")
    print(">>> EDIT")
    print(" ... task_id,field_name")
    print(" ... updated_value")

def help_update():
    os.system("cls")
    help_update_basic()
    input()

def help_update_basic():
    print("UPDATE: Allows user to update status_id value")
    print("Usage:")
    print(">>> UPDATE")
    print(" ... updated_value")

def help_sort():
    os.system("cls")
    help_sort_basic()
    input()

def help_sort_basic():
    print("SORT: Sorts tasks in ascending order by the given field")
    print("Usage:")
    print(">>> SORT")
    print(" ... sorting_field")

def help_sort_desc():
    os.system("cls")
    help_sort_desc_basic()
    input()

def help_sort_desc_basic():
    print("SORTDESC: Sorts tasks in descending order by the given field")
    print("Usage:")
    print(">>> SORTDESC")
    print(" ... sorting_field")

def help_clear():
    os.system("cls")
    help_clear_basic()
    input()

def help_clear_basic():
    print("CLEAR: Clears the given table")
    print("Usage:")
    print(">>> CLEAR")
    print(" ... table_to_clear")

def help_clear_hist():
    os.system("cls")
    help_clear_hist_basic()
    input()

def help_clear_hist_basic():
    print("CLEARHIST: Clears the task_history table")
    print("Usage:")
    print(">>> CLEARHIST")
    print(" ... table_to_clear")

def help_exit():
    os.system("cls")
    help_exit_basic()
    input()

def help_exit_basic():
    print("EXIT: Exits the program")
    print("Usage:")
    print(">>> EXIT")

def help_help():
    os.system("cls")
    help_help_basic()
    input()

def help_help_basic():
    print("HELP: Provides a description of functions and a usage statement")
    print("Usage:")
    print(">>> HELP function_name")
    print("or")
    print(">>> HELP page_number")

def print_separator():
    s = "-" * ROW_LENGTH
    print(s)
