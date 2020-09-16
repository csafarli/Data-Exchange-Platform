#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 23:34:09 2020

@author: c_safarli
"""

# -*- coding: utf-8 -*-
import os
from CustomerB import *
from DesignerB import *
from SupplierB import supplier

# Exit Screens
def delete3():
    screen4.destroy()

def delete_ue():
    screen_ue.destroy()

def delete_se():
    screen_se.destroy()


def delete4():
    screen5.destroy()

# Directing to the Sessions

def dashboardD():

    screen2.destroy()
    designerdb = designer()
    designerdb.run()

def dashboardC():

    screen2.destroy()
    customerdb = customer()
    customerdb.run()

def dashboardS():

    screen2.destroy()
    supplierdb = supplier()
    supplierdb.run()

#importlib.import_module('dash_supplier')

# global screen3
# screen3 = Toplevel()
# screen3.title("Success")
# screen3.geometry("150x100")

# Label (screen3, text = "").pack()
# Label (screen3, text = "Login Success!").pack()

# Label (screen3, text = "").pack()

# Button(screen3, text = "OK", command = delete2).pack()

# Alert Screens

def wrong_password():
    global screen4
    screen4 = Toplevel()
    screen4.title("Wrong password")
    screen4.geometry("350x300")

    Label(screen4, text="").pack()
    Label(screen4, text="Password is wrong! ").pack()

    Label(screen4, text="").pack()

    Button(screen4, text="OK", command=delete3).pack()

def userexist():

    global screen_ue
    screen_ue = Toplevel()
    screen_ue.title("User already exist!")
    screen_ue.geometry("350x300")

    Label(screen_ue, text="").pack()
    Label(screen_ue, text="Please insert valid username").pack()

    Label(screen_ue, text="").pack()

    Button(screen_ue, text="OK", command=delete_ue).pack()

def session_exist():

    global screen_se
    screen_se = Toplevel()
    screen_se.title("Designer exist!")
    screen_se.geometry("350x300")

    Label(screen_se, text="").pack()
    Label(screen_se, text="System has already a designer \n please register as different session").pack()

    Label(screen_se, text="").pack()

    Button(screen_se, text="OK", command=delete_se).pack()


def wrong_username():
    global screen5
    screen5 = Toplevel()
    screen5.title("Wrong username")
    screen5.geometry("350x300")

    Label(screen5, text="").pack()
    Label(screen5, text="Username is wrong! ").pack()

    Label(screen5, text="").pack()

    Button(screen5, text="OK", command=delete4).pack()


# Main Functions


def register_user():

    global username_info
    global password_info
    global session_info
    global listoffiles

    username_info = username.get()
    password_info = password.get()
    session_info = session_entry.get()

    listoffiles = os.listdir()

    if username_info + ".txt" in listoffiles:
        username_entry.delete(0, END)
        password_entry.delete(0, END)

        userexist()
    else:
        session_vrf()


def session_vrf():

    global verify_d
    session_list = []

    for file in listoffiles:

        if file.endswith(".txt"):
            fileln_d = open(file, "r")
            verify_d = fileln_d.read().splitlines()

            session_list.append(verify_d[2])

    if "Designer" in session_list:

        if session_info == "Designer":
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            session_exist()

        else:
            write_file()
    else:
        write_file()


def write_file():

    file = open(username_info + ".txt", "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write(session_info + "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Success! ", fg="green", font=("Calibri", 11)).pack()


def user_keyID():

    with open('Session', 'r') as file_s:
        verify_s = file_s.readlines()

        UserKEY = user_key
        verify_s[0] = UserKEY

    with open('Session', 'w') as file_s:
        file_s.writelines(verify_s)

global UserKEY

def login_vrfy():
    global usernameln
    global user_key
    usernameln = username_ln.get()
    passwordln = password_ln.get()

    username_entryln.delete(0, END)
    password_entryln.delete(0, END)

    list_of_files = os.listdir()

    if usernameln + ".txt" in list_of_files:
        fileln = open(usernameln + ".txt", "r")
        verify = fileln.read().splitlines()

        if passwordln in verify:

            user_key = verify[0]
            user_keyID()

            if verify[2] == "Designer":
                dashboardD()
            elif verify[2] == "Customer":
                dashboardC()
            else:
                dashboardS()

        else:
             wrong_password()

    else:
        wrong_username()


def register():
    global screen1

    screen1 = Toplevel()
    screen1.title("Register")
    screen1.geometry("350x300")

    global username
    global password
    global username_entry
    global password_entry
    global session_entry

    username = StringVar()
    password = StringVar()
    session_entry = StringVar()

    Label(screen1, text="Please fill the information below! ").pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()

    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()

    Label(screen1, text="").pack()

    Label(screen1, text="Select Session").pack()

    choices = {'Designer', 'Customer', 'Supplier'}
    session_entry.set('Supplier')

    DDMenu = OptionMenu(screen1, session_entry, *choices)
    DDMenu.pack()

    Label(screen1, text="").pack()

    Button(screen1, text="Register", height="1", width="10", command=register_user).pack()

    Label(screen1, text="").pack()


def login():
    global screen2
    global username_ln
    global password_ln
    global username_entryln
    global password_entryln

    username_ln = StringVar()
    password_ln = StringVar()

    screen2 = Toplevel()
    screen2.title("Login")
    screen2.geometry("300x250")

    Label(screen2, text="Please fill the information to login").pack()
    Label(screen2, text="").pack()

    Label(screen2, text="Username: ").pack()
    username_entryln = Entry(screen2, textvariable=username_ln)
    username_entryln.pack()
    Label(screen2, text="").pack()

    Label(screen2, text="Password: ").pack()
    password_entryln = Entry(screen2, textvariable=password_ln)
    password_entryln.pack()
    Label(screen2, text="").pack()

    Button(screen2, text="Login", height=1, width=10, command=login_vrfy).pack()


def main_screen():
    screen = Tk()
    screen.geometry("300x250")
    screen.title("User input")
    Label(text="User input", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(text="Login or Create new account").pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()

