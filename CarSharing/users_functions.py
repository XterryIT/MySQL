import pymysql
import os
import time


def login(cursor):
    print("Please enter your Email and Password to login in the system ")
    email = input("Write Email: ")
    login_password = input("Write Password: ")
                    

    #Here I`am send a requst to check what that person be in database `
    request = """ SELECT * FROM Users WHERE email = %s and password = %s """
    cursor.execute(request,(email, login_password))
    result = cursor.fetchall()

    if result:
        print("You are in the system!")
        time.sleep(2)
        os.system('cls')
        return email,login_password
    else:
        print("Somting wrong!")
        time.sleep(2)
        os.system('cls')



def regestration(cursor,connection):
    name = input("Write your name: ")
    surname = input("Write your surname: ")
    email = input("Write your email: ")
    password = input("Write your password: ")
    data = (name,surname,email,password)


    request = """ INSERT INTO Users(name, surname, email, password) VALUES (%s,%s,%s,%s) """
    cursor.execute(request,data)
    connection.commit()

    print("Your account was successfully created!!")
    time.sleep(2)
    os.system('cls')
    


def list_cars(cursor,connection):
    request = """ SELECT  """