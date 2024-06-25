import mysql.connector


def get_all_games() :
    speedscore_db = mysql.connector.connect (
        host = "localhost",
        user = "root",
        password = "",
        database = "workshop-web-s2"
    )

    if (speedscore_db.is_connected()):
        print("Connected")
    else:
        print("Not connected")

    bd_cursor = speedscore_db.cursor()
    # print(bd_cursor)
    # cursor = speedscore_db.cursor(buffered=True)
    toto = bd_cursor.execute("SELECT * FROM game").fetchall()
    print(toto)
    all_toto = toto.fetchall()
    return all_toto