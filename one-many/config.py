from datetime import datetime

host = 'localhost'
user = 'root'
password = ''
database = 'login'


def make_category():
    name = input("Type a name of new category:")
    
    return name 


def make_post():
    #here your typing a data of post
    name = input("Type a name of post:")
    title = input("Type a title of post:")
    text = input("Type a text of post:")
    photo = input("Type a directory and name of photo:")
    date = input("Type a date publication (Example: 2009-07-29):")
    catigories = input("Chose and type the number of catiegory your post:")


    #here I check the correctness of the filled data
    if not name.strip():
        print("!"*50)
        print("Name must be filled")
        print("!"*50)
    elif not title.strip():
        print("!"*50)
        print("Title must be filled")
        print("!"*50)
    elif not text.strip():
        print("!"*50)
        print("Text must be filled")
        print("!"*50)
    elif not photo.strip():
        print("!"*50)
        print("The direct of photo must be filled")
        print("!"*50)
    elif not catigories.strip():
        print("!"*50)
        print("Путь к фото не может быть пустым.")
        print("!"*50)
    else:
        from datetime import datetime

        def is_valid_date(date_str, format='%Y-%m-%d'):
            try:
                datetime.strptime(date_str, format)
                return True
            except ValueError:
                return False

        if not is_valid_date(date):
            print("!"*50)
            print("The data must be in format (Y-M-D)")
            print("!"*50)
        else:
            print("#"*50)
            print("All data is corect!")
    
    #here I am replacing the photo directory with the binary code of this photo 
    # so that there is no confusion when sending it to the database
    photo = convertToBinary(photo)


    return name,title,text,photo,date,catigories


#this function need to convert all file to binary
def convertToBinary(filename):
    with open(filename,'rb') as file:
        binarydata = file.read()
    return binarydata

#this function need to unconvert all binary code to file
def convertBinaryToFile(binarydata, filename):
    with open(filename,'wb') as file:
        file.write(binarydata)


