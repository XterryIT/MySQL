import pymysql
from config import host, user,password,database 

try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = database,
        cursorclass = pymysql.cursors.DictCursor 
    )
    print("SECSESFULLY conection to ", database)

    print("#" * 30)

    try:

        # #create a new table; relation one-one
        # with connection.cursor() as cursor:
        #     screate_table = "CREATE TABLE `users` (id int(11) AUTO_INCREMENT, first_name varchar(20) NOT NULL, last_name varchar(20)NOT NULL,  PRIMARY KEY(id));"
        #     create_table = "CREATE TABLE `passports` (id int(11) AUTO_INCREMENT,\
        #                                               passpot_number int(50) NOT NULL,\
        #                                               city_of_registration varchar(30) NOT NULL,\
        #                                               fk_passports_users int REFERENCES users(id),\
        #                                               PRIMARY KEY(id));"
        #     cursor.execute(create_table)
      
        # with connection.cursor() as cursor:
        #     cursor.execute("INSERT INTO users (first_name, last_name) VALUES ('Homer', 'Simpson');")
        #     cursor.execute("INSERT INTO users (first_name, last_name) VALUES ('Marge', 'Simpson');")
        #     cursor.execute("INSERT INTO users (first_name, last_name) VALUES ('Lisa', 'Simpson');")
        #     cursor.execute("INSERT INTO users (first_name, last_name) VALUES ('Bart', 'Simpson');")
        #     cursor.execute("INSERT INTO users (first_name, last_name) VALUES ('Megie', 'Simpson');")

        #     cursor.execute("INSERT INTO passports (passpot_number, city_of_registration, fk_passports_users) VALUES (1111, 'Sprinfield', 1);")
        #     cursor.execute("INSERT INTO passports (passpot_number, city_of_registration, fk_passports_users) VALUES (2222, 'Sprinfield', 2);")
        #     cursor.execute("INSERT INTO passports (passpot_number, city_of_registration, fk_passports_users) VALUES (3333, 'Sprinfield', 3);")
        #     cursor.execute("INSERT INTO passports (passpot_number, city_of_registration, fk_passports_users) VALUES (4444, 'Sprinfield', 4);")
        #     cursor.execute("INSERT INTO passports (passpot_number, city_of_registration, fk_passports_users) VALUES (5555, 'Sprinfield', 5);")

        #     connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT passpot_number FROM passports;")
            cursor.execute("SELECT users.first_name, passports.passpot_number FROM users,passports;")
            rows = cursor.fetchall()
            for row in rows:
                print(row)


    finally:
        connection.close()

except Exception as ex:
    print("NOT conection to", database)
    print(ex)