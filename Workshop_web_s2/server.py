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
    data = model.get_all_games()
    return render_template('games.html', games=data)
   
@app.route("/games/<id>") 
def game():
    return render_template('game.html', game=id)

@app.route("/account")
def account():
    return render_template('account.html')

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        password = model.hash_psw(request.form['password'])
        nationnality = request.form['nationality']
        user_add = model.add_user(email, username, password, nationnality)
        if user_add==True :
            return render_template('signin.html')
    
    return render_template('signup.html')

@app.route("/signin", methods=['GET','POST'])
def signin():
    if request.method == 'POST' : 
        username = request.form['user_name']
        data = model.get_test(username)
        return data   
        # username = request.form['user_name']
        # password = model.hash_psw(request.form['psw'])
        # if model.check_user_existence(username, password)==-1:
        #     message = "Votre nom d'utilisateur n'est pas bon"
        #     return render_template('signin.html', text = message)
        # if model.check_user_existence(username, password)==1:
        #     message = "Votre mot de passe n'est pas bon"
        #     return render_template('signin.html', text = message)
        # if model.check_user_existence(username, password)==0:
        #     return render_template('account.html')
    return render_template('signin.html')

@app.route("/ggg", methods=['GET','POST']) 
def test():
    username = request.form['user_name']
    data = model.get_test(username)
    return data

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



    
