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
    bd_cursor.close()
    connection.close()
    return True



def check_user_existence ( username, password ) :
    print('username ', username)
    connection = connect()
    SQL = "SELECT * FROM user WHERE username='%s'"
    bd_cursor = connection.cursor()
    bd_cursor.execute( SQL, username)
    data = bd_cursor.description
    print(data)
    # print('nb de ligne', bd_cursor.rowcount)
    # if bd_cursor.rowcount <1 :
    #     bd_cursor.close()
    #     connection.close()
    #     print('inconnu')
    #     return(-1)
    # user = bd_cursor.fetchone()
    # if password != user[3] :
    #     bd_cursor.close()
    #     connection.close()
    #     return(1)
    # if password == user[3] :
    #     bd_cursor.close()
    #     connection.close()
    #     return(0)


def get_test(username, password) :
    connection = connect()
    SQL = "SELECT * FROM user WHERE username=%s"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL, (username,))

    data = bd_cursor.fetchall() #values
    fields_list = bd_cursor.description   # keys
    formated_category = format_query(fields_list, data)
    if len(data)==0 :
        message = "le nom est incorect"
        return message
    if password == data[0][3] :
        message = "vous etes connecte"
        return message
    if password != data[0][3] :
        message = "le mot de passe est incorrect"
        return message
    bd_cursor.close()
    connection.close()
    return data







def get_all_users() :
    connection = connect()

    SQL = "SELECT * FROM user"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL)

    data = bd_cursor.fetchall() #values
    fields_list = bd_cursor.description  #keys
    formated_users = format_query(fields_list, data)

    bd_cursor.close()
    connection.close()
    return formated_users

def get_user(id) :
    connection = connect()
    SQL = "SELECT * FROM user where id_user = %s"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL, (id,))
    data = bd_cursor.fetchall() #values
    fields_list = bd_cursor.description  #keys
    formated_user = format_query(fields_list, data)
    bd_cursor.close()
    connection.close()
    return formated_user

def update_user(id, email, username, password, nationality) :
    try:
        connection = connect()
        if password != None :
            SQL = "update user set email = %s, username = %s, password = %s, nationality = %s where id_user = %s"
            bd_cursor = connection.cursor()
            bd_cursor.execute(SQL, (email, username, password, nationality, id))
        else : 
            SQL = "update user set email = %s, username = %s, nationality = %s where id_user = %s"
            bd_cursor = connection.cursor()
            bd_cursor.execute(SQL, (email, username, nationality, id))
        connection.commit()
    except Exception as e:
        print("An error occurred: {e}")
    finally:
        if bd_cursor:
            bd_cursor.close()
        if connection:
            connection.close()

def delete_one_user(id) :
    try:
        connection = connect()
        SQL = "delete from user where id_user = %s"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (id,))
        connection.commit()
    except Exception as e:
        print("An error occurred: {e}")
    finally:
        if bd_cursor:
            bd_cursor.close()
        if connection:
            connection.close()