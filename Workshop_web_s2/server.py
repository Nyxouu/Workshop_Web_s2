from flask import Flask,request,render_template,redirect
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
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = model.hash_psw(request.form['password'])
        nationnality = request.form['nationality'].strip()
        user_add = model.add_user(email, username, password, nationnality)
        if user_add==True :
            return render_template('signin.html')
    
    return render_template('signup.html')

@app.route("/signin", methods=['GET','POST'])
def signin():
    if request.method == 'POST' : 
        email = request.form['email'].strip()
        password = model.hash_psw(request.form['psw'])
        message = model.check_user_existence(email, password)
        if message == "ok" :
            return render_template('home.html')
        return render_template('signin.html', data=message)
    return render_template('signin.html')


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

@app.route("/users")
def users():
    data = model.get_all_users()
    return render_template('users.html', users=data)
   
@app.route("/users/<id>", methods=['GET']) 
def user(id):
    data = model.get_user(int(id))
    return render_template('profile.html', user=data)

@app.route("/users/edit/<id>", methods=['GET', 'POST'])
def edit_user(id):
    if request.method == 'POST' :
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        nationality = request.form['nationality'].strip()
        password = request.form['password']
        if password :
            hashed_password = model.hash_psw(password)
        else :
            hashed_password = None
        model.update_user(int(id), email, username, hashed_password, nationality)
    data = model.get_user(int(id))
    return render_template('edit_user.html', user=data)

@app.route("/users/delete/<id>", methods=['GET', 'POST'])
def delete_user(id):
    model.delete_one_user(int(id))
    return redirect("/users", code=302)