import mysql.connector


def get_all_games() :
    speedscore_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="workshop-web-s2"
    )
    SQL = "SELECT * FROM game"
    bd_cursor = speedscore_db.cursor()
    bd_cursor.execute(SQL)
    data = bd_cursor.fetchall()
    print(data)
    return data