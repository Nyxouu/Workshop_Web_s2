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

@app.route("/category/add", methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        label = request.form.get('label')
        description = request.form.get('description')
        model.add_new_category(label,description)
        # return redirect("/category", code=302)
    return render_template('category/form_category.html')

@app.route("/category/edit/<id>", methods=['GET', 'POST'])
def edit_category(id):
    if request.method == 'POST':
        label = request.form.get('label')
        description = request.form.get('description')
        model.update_category(id,label,description)
    category = model.get_category_from_id(id)
    return render_template('category/form_category.html', ctg=category)

@app.route("/category/delete/<id>")
def delete_category(id):
    model.delete_category_from_id(id)
    return redirect("/", code=302)


# ------------------------------------BACK OFFICE
# ---------SESSION
@app.route("/session/add")
def add_session():
    games = model.get_all_games()
    return render_template('session/add_session.html', games=games)

@app.route("/session/edit/<id>")
def edit_session():
    return render_template('session/edit_session.html')

@app.route("/session/delete/<id>")
def delete_session():
    return render_template('session/delete_session.html')