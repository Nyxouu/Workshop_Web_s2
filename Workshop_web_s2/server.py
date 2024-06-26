from flask import Flask,request,render_template,redirect
from flask_cors import CORS
import model

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    games_per_category = model.get_number_of_games_per_category()
    sessions_per_category = model.get_number_of_sessions_per_category()
    infos_categories = model.combine_infos_categories(games_per_category, sessions_per_category)
    return render_template('home.html', infos_categories=infos_categories)

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


# ---------------------------------------------------------------------------
# ---------------------------- Games
# ---------------------------------------------------------------------------

@app.route("/testadd")
def testadd():
    model.add_liaison_gc(1,1)
    return redirect("/", code=302)
@app.route("/testdel")
def testdel():
    model.delete_liaison_gc(1,1)
    return redirect("/", code=302)

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
        ctgs = request.form.getlist('category[]')
        ctgs = [int(c) for c in ctgs]
        model.add_new_game(name, description, released_date, image)
        id_new_game = model.get_latest_game_id()[0]
        for ctg in ctgs:
            model.add_liaison_gc(id_new_game,ctg)
    ctgs = model.get_all_category()
    return render_template('game/form_game.html', all_ctgs=ctgs)

@app.route("/games/edit/<id>", methods=['GET', 'POST'])
def edit_game(id):
    if request.method == 'POST' :
        name = request.form['name']
        description = request.form['description']
        released_date = request.form['released_date']
        image = request.form['image']
        model.update_game(int(id), name, description, released_date, image)
    data = model.get_game(int(id))
    ctgs = model.get_all_category()
    game_ctgs = model.get_categories_from_game_id(int(id))
    print(game_ctgs)
    return render_template('game/form_game.html', game=data, all_ctgs=ctgs, game_ctgs=game_ctgs)

@app.route("/games/delete/<id>", methods=['GET', 'POST'])
def delete_game(id):
    model.delete_one_game(int(id))
    return redirect("/games", code=302)

# ---------------------------------------------------------------------------
# ---------------------------- Category
# ---------------------------------------------------------------------------

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

