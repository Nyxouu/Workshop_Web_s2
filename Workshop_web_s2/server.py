from flask import Flask,request,render_template
from flask_cors import CORS
import model

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template('home.html')

@app.route("/games")
def games():
    all_games = model.get_all_games()
    return render_template('games.html', games=all_games)
   
@app.route("/games/<id>") 
def game():
    return render_template('game.html', game=id)

@app.route("/account")
def account():
    return render_template('account.html')

@app.route("/favorites")
def favorites():
    return render_template('favorites.html')

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')
