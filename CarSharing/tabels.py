
# This is what my database should look like
# Users {
# 	users_id integer pk increments *>* booking.fk_users_id
# 	name char(20)
# 	surname char(20)
# 	email char(100)
# 	password char(200)
# }

# Cars {
# 	regestration_id char(8) pk *>* booking.fk_regestration_id
# 	brand char(20)
# 	model char(20)
# 	seats int(2)
# 	year int(4)
# 	prise int(5)
# 	notes text
# 	photo longblob
# 	is_repair bool def(False)
# 	is_booked bool def(False)
# }

# Damage {
# 	damage_id integer pk increments
# 	description text
# 	prise int(8)
# 	fk_regestration_id integer *> Cars.regestration_id
# }

# booking {
# 	booking_id integer pk increments
# 	fk_users_id integer
# 	fk_regestration_id char(8)
# 	start_date datetime
# 	end_date datetime
# }



# This is SQL request to create a databse
Users = """ CREATE TABLE `Users` (
        users_id int AUTO_INCREMENT NOT NULL,
        name char(20),
        surname char(20),
        email char(100),
        password char(200),
        PRIMARY KEY(users_id)
) """

Cars = """ CREATE TABLE `Cars` (
        reg_id char(8) NOT NULL,
        brand char(20) NOT NULL,
        model char(20) NOT NULL,
        seats int(2) NOT NULL,
        year int(4) NOT NULL,
        prise int(5) NOT NULL,
        notes text NOT NULL,
        photo longblob NOT NULL,
        status BOOLEAN DEFAULT 1 NOT NULL,
        PRIMARY KEY(reg_id)
);"""

Damage = """ CREATE TABLE `Damage` (
        damage_id int NOT NULL AUTO_INCREMENT,
        description text NOT NULL,
        prise int(8) NOT NULL,
        fk_reg_id char(8) NOT NULL,
        PRIMARY KEY(damage_id),
        FOREIGN KEY (fk_reg_id) REFERENCES Cars(reg_id)
) """

Booking = """ CREATE TABLE `Booking` (
        booking_id int NOT NULL AUTO_INCREMENT,
        fk_users_id int NOT NULL,
        fk_reg_id char(8) NOT NULL,
        start_date datetime NOT NULL, 
        end_date datetime NOT NULL, 
        PRIMARY KEY (booking_id),
        FOREIGN KEY (fk_users_id) REFERENCES Users(users_id),
        FOREIGN KEY (fk_reg_id) REFERENCES Cars(reg_id),
        CHECK (start_date < end_date)
)"""