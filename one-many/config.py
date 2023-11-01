from datetime import datetime

host = 'localhost'
user = 'root'
password = ''
database = 'login'


def make_category():
    name = input("Type a name of new category:")
    
    return name 


def make_post():

    name = input("Type a name of post:")
    title = input("Type a title of post:")
    text = input("Type a text of post:")
    photo = input("Type a directory and name of photo:")
    date = input("Type a date publication (Example: 2009-07-29):")



    if not name.strip():
        print("Name must be filled")
    elif not title.strip():
        print("Title must be filled")
    elif not text.strip():
        print("Text must be filled")
    elif not photo.strip():
        print("Путь к фото не может быть пустым.")
    else:
        from datetime import datetime

        def is_valid_date(date_str, format='%Y-%m-%d'):
            try:
                datetime.strptime(date_str, format)
                return True
            except ValueError:
                return False

        if not is_valid_date(date):
            print("The data must be in format (Y-M-D)")
        else:
            print("All data is corect!")



def convertToBinary(filename):
    with open(filename,'rb') as file:
        binarydata = file.read()
    return binarydata


def convertBinaryToFile(binarydata, filename):
    with open(filename,'wb') as file:
        file.write(binarydata)