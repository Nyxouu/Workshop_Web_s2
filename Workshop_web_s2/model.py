import mysql.connector
import hashlib

def format_query(keys, values):
    column_names = [field[0] for field in keys]
    result = []
    for row in values:
        row_dict = dict(zip(column_names, row))
        result.append(row_dict)
    return result
    
def connect():
    speedscore_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="workshop-web-s2"
    )
    return speedscore_db


def get_all_games() :
    connection = connect()
    SQL = "SELECT * FROM game"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL)

    data = bd_cursor.fetchall() #values
    fields_list = bd_cursor.description   # keys

    formated_games = format_query(fields_list, data)

    bd_cursor.close()
    connection.close()
    return formated_games

def hash_psw(psw):
   return hashlib.sha256(str(psw).encode('utf-8')).hexdigest()

def add_user(email, username, password, nationality) :
    connection = connect()
    SQL = "INSERT INTO user (email,username, password,nationality) VALUES (%s,%s,%s,%s)"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL, (email, username, password, nationality))
    connection.commit()

    fields_list = bd_cursor.description  #keys

    bd_cursor.close()
    connection.close()
    return True