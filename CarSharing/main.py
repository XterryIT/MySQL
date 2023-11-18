import os
from functions import login, regestration
import pymysql
from tabels import * 
from config import host,user,password,database


def main():
    try:
    #conection to database
        connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = database,
        cursorclass = pymysql.cursors.DictCursor 
        )

        
    #inplementing code
        try:
            with connection.cursor() as cursor:

                #Here I`am want to that person to loggin in my app 
                while(True):
                    print("Welcome to application CarSharing")
                    print("You want Login (1) or regestration account (2)?")
                    chose = int(input("Your answer: "))
                    os.system('cls')
                    
                    if chose == 1:
                        login(cursor)            

                    elif chose == 2:
                        regestration(cursor,connection)


















    #closing the session
        finally:
            connection.close()


#tracking and print the all kinds Erors
    except Exception as ex:
        print("NOT conection to", database)
        print(ex)



   


if __name__ == '__main__':
    main()