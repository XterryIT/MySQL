import functions
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
                cursor.execute(Booking)
                connection.commit()


    #closing the session
        finally:
            connection.close()


#tracking and print the all kinds Erors
    except Exception as ex:
        print("NOT conection to", database)
        print(ex)


if __name__ == '__main__':
    main()