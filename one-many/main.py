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
        while True:
            print("Make a new Post - 1")
            print("Make a new category - 2")
            print("Show the posts one of the category - 3")
            print("End - 4")
            choice = input("Your answer: ")


            # add a new data in database posts
            if choice == "1":
                print("#" * 50)
                print("Choose the category of your next post and then write the number below")
                cursor.execute("SELECT * FROM `catiegories`")
                rows = cursor.fetchall()
                for row in rows:
                    for key, value in row.items():
                        print(f"{value}", end="  |  ")
                    print()
                    

                #Upload a new post to database 
                print("#"*50)
                name,title,text,photo,date,catiegories=make_post()
                post_data = (name,title,text,photo,date,catiegories)
                insert_querry = "INSERT INTO posts (post_name, post_title, post_text, post_photo, post_date, fk_posts_catiegories) VALUES (%s,%s,%s,%s,%s,%s);"
                cursor.execute(insert_querry,post_data)
                connection.commit()




            #add a new category in database category
            elif choice == "2":
                name = make_category()
                insert_querry = "INSERT INTO catiegories (name) VALUES (%s);"
                try:
                    cursor.execute(insert_querry,name)
                    connection.commit()
                    print("The data was sucsessfuly uploaded")
                    print("#" * 50)
                except pymysql.Connection.Error as e:
                    print(f"You type a wrong data!")

            

            elif choice == "3":
                print("#" * 50)

                cursor.execute("SELECT * FROM `catiegories`")
                rows = cursor.fetchall()
                for row in rows:
                    for key, value in row.items():
                        print(f"{value}", end="  |  ")
                    print()
                    

                print("#"*50)

                chose = int(input("Select the category of posts you want to read: "))

                cursor.execute("SELECT id FROM `catiegories`")
                rows = cursor.fetchall()
                id_values = [item['id'] for item in rows]
                
                if chose in id_values:
                    num = str(chose)
                    request = """ SELECT post_name FROM `posts` WHERE fk_posts_catiegories = %s """
                    cursor.execute(request, chose)
                    category = cursor.fetchall()

                    print("#"*30)
                    for item in category:
                        print(item['post_name'])
                    print("#"*30)
                else:
                    print("Incorect number")

                









            elif choice == "4":
                break


            else: 
                print("Incorect number!")
                break



    #closing the session
    finally:
        connection.close()


#tracking and print the all kinds Erors
except Exception as ex:
    print("NOT conection to", database)
    print(ex)