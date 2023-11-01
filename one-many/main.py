import pymysql
from config import host, user,password,database, make_post, make_category, convertToBinary,convertBinaryToFile


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
    print("SECSESFULLY conection to", database)

    print("#" * 50)



    #inplementing code
    try:
                # #creation of tables
        # with connection.cursor() as cursor:
        #     table2 = "CREATE TABLE catiegories(id int(11) NOT NULL AUTO_INCREMENT,\
        #                                        name VARCHAR(200) NOT NULL,\
        #                                        PRIMARY KEY(id));"



        #     table = "CREATE TABLE posts(id int(11) NOT NULL AUTO_INCREMENT,\
        #                                 post_name VARCHAR(200) NOT NULL,\
        #                                 post_title VARCHAR(200) NOT NULL,\
        #                                 post_text VARCHAR(200) NOT NULL,\
        #                                 post_photo BLOB NOT NULL,\
        #                                 post_date DATE NOT NULL,\
        #                                 fk_posts_catiegories int(11) REFERENCES catiegories(id),\
        #                                 PRIMARY KEY(id))"
            
        #     cursor.execute(table)
        #     print("sucess!")



         cursor = connection.cursor()
        # while True:
        #     print("Make a new Post - 1")
        #     print("Make a new category - 2")
        #     print("End - 3")
        #     choice = input("Your answer: ")


        #     # add a new data in database posts
        #     if choice == "1":
        #         pass



        #     #add a new category in database category
        #     elif choice == "2":
        #         name = make_category()
        #         insert_querry = "INSERT INTO catiegories (name) VALUES (%s);"
        #         try:
        #             cursor.execute(insert_querry,name)
        #             connection.commit()
        #             print("The data was sucsessfuly uploaded")
        #             print("#" * 50)
        #         except pymysql.Connection.Error as e:
        #             print(f"You type a wrong data!")

            

        #     elif choice == "3":
        #         break


        #     else: 
        #         print("Incorect number!")
        #         break

        photo = 
        



    #closing the session
    finally:
        connection.close()


#tracking and print the all kinds Erors
except Exception as ex:
    print("NOT conection to", database)
    print(ex)