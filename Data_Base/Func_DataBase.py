import sqlite3


def Create_DataBase(Place="./main_information.db"):
    conection = sqlite3.connect(Place)
    cursor = conection.cursor()
    sql_source = """
        CREATE TABLE IF NOT EXISTS information (
            Id INTEGER,
            amount INTEGER ,
            Type_Amount VARCHAR(10) ,
            From_To VARCHAR(15) ,
            date_amount VARCHAR(15) ,
            Description VARCHAR(60)
        );
    """

    cursor.execute(sql_source)
    conection.commit()
    conection.close()


def Add_in_DataBase(Id, Amount, type_amount, FromOrTo, Date_To, Description):
    conection = sqlite3.connect("./main_information.db")
    cursor = conection.cursor()
    sql_source = "INSERT INTO  information VALUES (?,?,?,?,?,?)"
    cursor.execute(sql_source, (Id, Amount, type_amount,
                                FromOrTo, Date_To, Description))

    conection.commit()
    conection.close()


def Search_in_DataBase(Place="./main_information.db"):
    conection = sqlite3.connect(Place)
    cursor = conection.cursor()
    sql_source = " SELECT * FROM information ;"
    cursor.execute(sql_source)

    for i in cursor:
        yield i

    conection.commit()
    conection.close()


def Delate_in_DataBase(Place="./main_information.db"):
    conection = sqlite3.connect(Place)
    cursor = conection.cursor()
    sql_source = "DROP TABLE information"
    cursor.execute(sql_source)
    conection.commit()
    conection.close()

def Delate_item_in_DataBase(amount,Type_Amount,From_To,date_amount,Description,Place="./main_information.db"):
    conection = sqlite3.connect(Place)
    cursor = conection.cursor()
    sql_source = "DELETE FROM information WHERE amount=? AND Type_Amount=? AND From_To=? AND date_amount=? AND Description=?"
    cursor.execute(sql_source,(amount,Type_Amount,From_To,date_amount,Description))
    conection.commit()
    conection.close()

def get_password_in_database(Place="./main_information.db"):
    conection = sqlite3.connect(Place)
    cursor = conection.cursor()
    sql_source = " SELECT * FROM Password ;"
    cursor.execute(sql_source)

    password = ""

    for i in cursor:
        password = i[0]

    conection.commit()
    conection.close()

    return password


def delate_password(Place="./main_information.db"):
    conection = sqlite3.connect(Place)
    cursor = conection.cursor()
    delete_table = "DROP TABLE Password"
    try:
        cursor.execute(delete_table)
    except:
        pass
    conection.commit()
    conection.close()


def Data_Base_Password(password, Place="./main_information.db"):
    conection = sqlite3.connect(Place)
    cursor = conection.cursor()

    delate_password()

    creat_table = """
        CREATE TABLE IF NOT EXISTS Password (
            password VARCHAR
        );
    """
    add_password = "INSERT INTO  Password (password) VALUES (?)"

    cursor.execute(creat_table)
    cursor.execute(add_password, (password,))

    conection.commit()
    conection.close()


def set_setting(win):
    import json
    from PyQt5 import QtGui
    try:
        with open("setting.json", 'r') as File:
            File = json.load(File)

            font = QtGui.QFont()
            font.setFamily(File["type_font"])
            font.setPointSize(int(File["size_font"]))
            win.setFont(font)
    except:
        print("Json Not Found")


