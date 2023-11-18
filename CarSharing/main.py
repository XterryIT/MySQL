import os
import pymysql
from tabels import * 
from config import host,user,password,database
from users_functions import login, regestration
from admin_functions import add_car

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
                exit = True
                while(True):

                    #Here I`am want to that person to loggin in my app 
                    print("Welcome to application CarSharing")
                    print("You want Login (1) or regestration account (2)?")
                    chose = int(input("Your answer: "))
                    os.system('cls')
                    

                    # Login in app
                    if chose == 1:
                        temp1, temp2 = login(cursor)

                        #Here I chek reterned email and password, if its admin I start a admin panel
                        if temp1 == "root" and temp2 == "0000":

                            #This is admin panel
                            while(True):
                                print("-"*50)
                                print("ADMIN PANEL")
                                print("-"*50)
                                print("Add a car (1)")
                                print("Exit (2)")
                                chose_admin = int(input("Your answer: "))

                                if chose_admin == 1:
                                    add_car(cursor,connection)
                                
                                #Exit from admin Panel
                                if chose_admin == 2:
                                    exit = False
                                    break

                        else: 
                            pass
                    
                    #When You Exit from Admin Panel, the app woll stoped
                    if exit == False : break

                    #If a person does not have an account, he must be created here
                    elif chose == 2:
                        regestration(cursor,connection)




                    # Here I open acces to the application after login or regestration
                    print("-"*50)
                    print("Welcome to CarSharing")
                    print("-"*50)
                    print("list of available cars (1)")
                    print("Book a car (2)")
                    chose = int(input("Your answer: "))

                    if chose == 1:
                        pass

                    if chose == 2:
                        pass



















    #closing the session
        finally:
            connection.close()


#tracking and print the all kinds Erors
    except Exception as ex:
        print("NOT conection to", database)
        print(ex)



   




if __name__ == '__main__':
    main()