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

# ---------------------------------------------------------------------------
# ---------------------------- Users
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# ---------------------------- Connexion/Inscription/Comptes
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# ---------------------------- Games
# ---------------------------------------------------------------------------

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
        name = request.form['name'].strip()
        description = request.form['description'].strip()
        released_date = request.form['released_date']
        image = request.form['image'].strip()
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
        name = request.form['name'].strip()
        description = request.form['description'].strip()
        released_date = request.form['released_date']
        image = request.form['image'].strip()
        model.update_game(int(id), name, description, released_date, image)

        #gestion category
        previous_ctgs = model.get_categories_from_game_id(int(id))
        # previous_ctgs = [ctg['id_category'] for ctg in previous_ctgs]
        new_ctgs = request.form.getlist('category[]')
        new_ctgs = [int(c) for c in new_ctgs]

        for previous_ctg in previous_ctgs:
            if previous_ctg not in new_ctgs:
                model.delete_liaison_gc(id, previous_ctg)

        for new_ctg in new_ctgs:
            if new_ctg not in previous_ctgs:
                model.add_liaison_gc(id, new_ctg)

    data = model.get_game(int(id))
    ctgs = model.get_all_category()
    game_ctgs = model.get_categories_from_game_id(int(id))
    # game_ctgs = [ctg['id_category'] for ctg in game_ctgs]
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
        label = request.form.get('label').strip()
        description = request.form.get('description').strip()
        model.add_new_category(label,description)
        # return redirect("/category", code=302)
    return render_template('category/form_category.html')

@app.route("/category/edit/<id>", methods=['GET', 'POST'])
def edit_category(id):
    if request.method == 'POST':
        label = request.form.get('label').strip()
        description = request.form.get('description').strip()
        model.update_category(id,label,description)
    category = model.get_category_from_id(id)
    return render_template('category/form_category.html', ctg=category)

@app.route("/category/delete/<id>")
def delete_category(id):
    model.delete_category_from_id(id)
    return redirect("/", code=302)


# ---------------------------------------------------------------------------
# ---------------------------- Session
# ---------------------------------------------------------------------------

@app.route("/session/add")
def add_session():
    games = model.get_all_games()
    return render_template('session/form_session.html', games=games)

@app.route("/session/edit/<id>")
def edit_session():
    return render_template('session/form_session.html')

@app.route("/session/delete/<id>")
def delete_session():
    return render_template('session/delete_session.html')

