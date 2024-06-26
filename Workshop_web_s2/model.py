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

# ---------------------------------------------------------------------------
# ---------------------------- Game_Category
# ---------------------------------------------------------------------------
def add_liaison_gc(id_game, id_category) :
    try:
        connection = connect()
        SQL = "insert into game_category values (%s, %s)"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (id_game, id_category))
        connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if bd_cursor:
            bd_cursor.close()
        if connection:
            connection.close()
def delete_liaison_gc(id_game, id_category) :
    try:
        connection = connect()
        SQL = "delete from game_category where _id_game = %s and _id_category = %s"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (id_game, id_category))
        connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if bd_cursor:
            bd_cursor.close()
        if connection:
            connection.close()

def get_categories_from_game_id(id_game) :
    connection = connect()
    SQL = "select id_category from category join game_category on category.id_category=game_category._id_category where game_category._id_game = %s"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL, (id_game,))

    data = bd_cursor.fetchall() #values
    data = [row[0] for row in data]
    # fields_list = bd_cursor.description   # keys
    # formated_category = format_query(fields_list, data)
    bd_cursor.close()
    connection.close()
    return data

# ---------------------------------------------------------------------------
# ---------------------------- Games 
# ---------------------------------------------------------------------------
def get_all_games() :
    connection = connect()

    SQL = "SELECT * FROM game"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL)

    data = bd_cursor.fetchall() #values
    fields_list = bd_cursor.description  #keys
    formated_games = format_query(fields_list, data)

    bd_cursor.close()
    connection.close()
    return formated_games

def get_latest_game_id() :
    connection = connect()
    SQL = "SELECT id_game FROM game ORDER BY id_game DESC LIMIT 1"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL)
    data = bd_cursor.fetchone()
    bd_cursor.close()
    connection.close()
    return data

def get_game(id) :
    connection = connect()
    SQL = "SELECT * FROM game where id_game = %s"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL, (id,))
    data = bd_cursor.fetchall() #values
    fields_list = bd_cursor.description  #keys
    formated_game = format_query(fields_list, data)
    bd_cursor.close()
    connection.close()
    return formated_game

def add_new_game(name, description, released_date, image) :
    try:
        connection = connect()
        SQL = "insert into game (name, description, released_date, image) values (%s, %s, %s, %s)"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (name, description, released_date, image))
        connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if bd_cursor:
            bd_cursor.close()
        if connection:
            connection.close()

def update_game(id, name, description, released_date, image) :
    try:
        connection = connect()
        SQL = "update game set name = %s, description = %s, released_date = %s, image = %s where id_game = %s"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (name, description, released_date, image, id))
        connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if bd_cursor:
            bd_cursor.close()
        if connection:
            connection.close()

def delete_one_game(id) :
    try:
        connection = connect()
        SQL = "delete from game where id_game = %s"
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

# ---------------------------------------------------------------------------
# ---------------------------- Category
# ---------------------------------------------------------------------------
def get_all_category():
    connection = connect()
    SQL = "SELECT id_category,label FROM category"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL)
    data = bd_cursor.fetchall() #values
    fields_list = bd_cursor.description   # keys
    formated_category = format_query(fields_list, data)
    bd_cursor.close()
    connection.close()
    return formated_category

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