import mysql.connector

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

def add_new_category(label,description):
    try:
        connection = connect()
        SQL = "INSERT INTO category (label, description) VALUES (%s, %s)"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (label, description))
        connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if bd_cursor:
            bd_cursor.close()
        if connection:
            connection.close()

def get_category_from_id(id):
    connection = connect()
    SQL = "SELECT * FROM category WHERE id_category = %s"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL, (id,))

    data = bd_cursor.fetchall() #values
    fields_list = bd_cursor.description   # keys
    formated_category = format_query(fields_list, data)
    bd_cursor.close()
    connection.close()
    return formated_category

def update_category(id,label,description):
    try:
        connection = connect()
        SQL = "update category set label = %s, description = %s where id_category = %s"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (label, description, int(id)))
        connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if bd_cursor:
            bd_cursor.close()
        if connection:
            connection.close()

def delete_category_from_id(id):
    try:
        connection = connect()
        SQL = "delete from category where id_category = %s"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (id,))
        connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if bd_cursor:
            bd_cursor.close()
        if connection:
            connection.close()