from flask import Flask,request,render_template,redirect
from flask_cors import CORS
import model

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template('home.html')

# @app.route("/account")
# def account():
#     return render_template('account.html')

# @app.route("/favorites")
# def favorites():
#     return render_template('favorites.html')

# @app.route("/signin")
# def signin():
#     return render_template('signin.html')

# @app.route("/signup")
# def signup():
#     return render_template('signup.html')

# @app.route("/category/add")
# def signup():
#     return render_template('signup.html')
# @app.route("/category/edit/<id>")
# def signup():
#     return render_template('signup.html')
# @app.route("/category/delete/<id>")
# def signup():
#     return render_template('signup.html')

@app.route("/games")
def games():
    data = model.get_all_games()
    return render_template('game/games.html', games=data)
   
@app.route("/games/<id>", methods=['GET']) 
def game(id):
    data = model.get_game(int(id))
    return render_template('game/game.html', game=data)

@app.route("/games/add", methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST' :
        name = request.form['name']
        description = request.form['description']
        released_date = request.form['released_date']
        image = request.form['image']
        model.add_new_game(name, description, released_date, image)
    return render_template('game/add_game.html')

@app.route("/games/edit/<id>", methods=['GET', 'POST'])
def edit_game(id):
    data = model.get_game(int(id))
    if request.method == 'POST' :
        name = request.form['name']
        description = request.form['description']
        released_date = request.form['released_date']
        image = request.form['image']
        model.update_game(int(id), name, description, released_date, image)
        data = model.get_game(int(id))
    return render_template('game/edit_game.html', game=data)

@app.route("/games/delete/<id>", methods=['GET', 'POST'])
def delete_game(id):
    model.delete_one_game(int(id))
    return redirect("/games", code=302)