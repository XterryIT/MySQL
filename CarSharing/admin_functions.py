import os
import time

#this function need to convert all file to binary
def convertToBinary(filename):
    with open(filename,'rb') as file:
        binarydata = file.read()
    return binarydata

#this function need to unconvert all binary code to file
def convertBinaryToFile(binarydata, filename):
    with open(filename,'wb') as file:
        file.write(binarydata)




def add_car(cursor,connection):
    regestration = input("Type a number regestration car: ")
    brand = input("Type a brand of car: ")
    model = input("Type a model of car: ")
    seats = input("Type how many seats in car: ")
    year = input("Type year of car: ")
    prise = input("Type the car rental price (per hour $): ")
    notes = input("Type a notes for the car: ")
    photo = input("Type a directory of car photo: ")
    repair = input("Type 0 or 2 (0 is mean everything is fine with the car) (2 is mean the car broke): ")
    booked = input("Type 0 (thats mean a car is avalibele to book): ")
    

    binary = convertToBinary(photo)

    data = (regestration, brand, model, seats, year, prise, notes, binary, repair, booked)
    request = """ INSERT INTO Cars(reg_id,brand, model, seats, year, prise, notes, photo, is_repair, is_booked) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
    cursor.execute(request,data)
    connection.commit()

    print("Added a new car!!!")
    time.sleep(2)
    os.system('cls')






