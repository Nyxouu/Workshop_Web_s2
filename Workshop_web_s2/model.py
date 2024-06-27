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

def hash_psw(psw):
   return hashlib.sha256(str(psw).encode('utf-8')).hexdigest()

# ---------------------------------------------------------------------------
# ---------------------------- Users
# ---------------------------------------------------------------------------

def get_user_from_email(email) :
    connection = connect()
    SQL = "SELECT * FROM user WHERE email=%s"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL, (email,))

    data = bd_cursor.fetchall() #values
    fields_list = bd_cursor.description   # keys
    formated_category = format_query(fields_list, data)
    
    bd_cursor.close()
    connection.close()
    return formated_category

def check_user_existence(email, password) :
    data = get_user_from_email(email)
    if len(data)==0 :
        message = "le nom est incorect"
        return message
    if password != data[0]['password'] :
        message = "le mot de passe est incorrect"
        return message
    if password == data[0]['password'] :
        message = "ok"
        return message
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

def add_user(email, username, password, nationality) :
    connection = connect()
    SQL = "INSERT INTO user (email,username, password,nationality) VALUES (%s,%s,%s,%s)"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL, (email, username, password, nationality))
    connection.commit()
    bd_cursor.close()
    connection.close()
    return True

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

def search_games_by_name(game_name):
    connection = connect()
    SQL = "SELECT * FROM game WHERE LOWER(name) LIKE %s"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL, ('%' + game_name.lower() + '%',)) 
    data = bd_cursor.fetchall()
    fields_list = bd_cursor.description
    formated_games = format_query(fields_list, data)
    bd_cursor.close()
    connection.close()
    return formated_games

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
        # suppression des sessions utilisant le jeu à supprimer
        SQL = "delete from session where _id_game = %s"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (id,))

        # suppression des game_category utilisant le jeu à supprimer
        SQL = "delete from game_category where _id_game = %s"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (id,))

        # suppression du jeu
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

def get_categories_from_game_id(idGame):
    connection = connect()
    SQL = "SELECT id_category,label FROM category JOIN game_category ON category.id_category=game_category._id_category WHERE game_category._id_game = %s"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL, (idGame,))

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
        # suppression des sessions utilisant la catégorie à supprimer
        SQL = "delete from session where _id_category = %s"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (id,))

        # suppression des game_category utilisant la catégorie à supprimer
        SQL = "delete from game_category where _id_category = %s"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (id,))

        # suppression de la catégorie
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

def get_number_of_games_per_category() : 
    connection = connect()
    SQL = "SELECT category.label, COALESCE(COUNT(game_category._id_game), 0) as nb_of_games FROM category LEFT JOIN game_category ON category.id_category = game_category._id_category GROUP BY category.id_category, category.label order by category.label asc;"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL)

    data = bd_cursor.fetchall() #values
    fields_list = bd_cursor.description #keys
    formated_category_games = format_query(fields_list, data)
    bd_cursor.close()
    connection.close()
    return formated_category_games

def get_number_of_sessions_per_category() :
    connection = connect()
    SQL = "SELECT category.label, COALESCE(COUNT(session.id_session), 0) as nb_of_sessions FROM category LEFT JOIN session ON category.id_category = session._id_category GROUP BY category.id_category, category.label order by category.label asc;"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL)

    data = bd_cursor.fetchall() #values
    fields_list = bd_cursor.description #keys
    formated_session_category = format_query(fields_list, data)
    bd_cursor.close()
    connection.close()
    return formated_session_category

def combine_infos_categories(games_per_category, sessions_per_category):
    combined_dict = {}

    for game in games_per_category:
        label = game['label']
        nb_of_games = game['nb_of_games']
        combined_dict[label] = {'label': label, 'nb_of_games': nb_of_games, 'nb_of_sessions': 0}

    for session in sessions_per_category:
        label = session['label']
        nb_of_sessions = session['nb_of_sessions']
        if label in combined_dict:
            combined_dict[label]['nb_of_sessions'] = nb_of_sessions
        else:
            combined_dict[label] = {'label': label, 'nb_of_games': 0, 'nb_of_sessions': nb_of_sessions}

    combined_list = list(combined_dict.values())
    return combined_list

# ---------------------------------------------------------------------------
# ---------------------------- Session
# ---------------------------------------------------------------------------

def get_all_sessions():
    connection = connect()

    SQL = "SELECT * FROM session"
    bd_cursor = connection.cursor()
    bd_cursor.execute(SQL)

    data = bd_cursor.fetchall() #values
    fields_list = bd_cursor.description  #keys
    formated_sessions = format_query(fields_list, data)

    bd_cursor.close()
    connection.close()
    return formated_sessions

def add_new_session(time, date, game, user, ctg):
    try:
        connection = connect()
        SQL = "INSERT INTO session (time, date, _id_game, _id_user, _id_category) VALUES (%s, %s, %s, %s, %s)"
        bd_cursor = connection.cursor()
        bd_cursor.execute(SQL, (time, date, game, user, ctg))
        connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if bd_cursor:
            bd_cursor.close()
        if connection:
            connection.close()

def delete_session_from_id(id):
    try:
        connection = connect()
        SQL = "delete from session where id_session = %s"
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









