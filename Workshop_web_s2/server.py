from flask import Flask,request,render_template,redirect, session
from flask_cors import CORS
from datetime import date as dt
import model
import os


app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')
CORS(app)

@app.route("/")
def index():
    games_per_category = model.get_number_of_games_per_category()
    sessions_per_category = model.get_number_of_sessions_per_category()
    infos_categories = model.combine_infos_categories(games_per_category, sessions_per_category)
    return render_template('home.html', infos_categories=infos_categories)
# ---------------------------------------------------------------------------
# ---------------------------- Admin
# ---------------------------------------------------------------------------

@app.route("/admin_games")
def admin_games():
    data = model.get_all_games()
    return render_template('admin/games/admin_games.html', games=data)

@app.route("/games/admin/<id>", methods=['GET']) 
def admin_game(id):
    data = model.get_game(int(id))
    return render_template('admin/games/admin_game.html', game=data)

@app.route("/admin_categories")
def admin_categories():
    data = model.get_all_category()
    print (data)
    return render_template('admin/categories/admin_categories.html', categories=data)

@app.route("/admin_sessions")
def admin_sessions():
    return render_template('admin/sessions/admin_sessions.html')

@app.route("/admin_users")
def admin_users():
    return render_template('admin/users/admin_users.html')



@app.route("/search", methods=['GET'])
def search():
    if request.method == 'GET':
        game_name = request.args.get('games-search')
        games = model.search_games_by_name(game_name)
        return render_template('game/games.html', games=games)
    return

# ---------------------------------------------------------------------------
# ---------------------------- Users
# ---------------------------------------------------------------------------

@app.route("/users")
def users():
    data = model.get_all_users()
    return render_template('user/users.html', users=data)
   
@app.route("/users/<id>", methods=['GET']) 
def user(id):
    data = model.get_user(int(id))
    if data[0]['admin']==1 :
        return render_template('admin/admin_profile.html', user=data)
    return render_template('user/profile.html', user=data)

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
    return render_template('user/edit_user.html', user=data)

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
        if len(model.get_user_from_email(email)) > 0:
            error = "un compte existe deja avec cet email."
            return render_template('user/signup.html', message = error)
        password = model.hash_psw(request.form['password'])
        nationnality = request.form['nationality'].strip()
        user_add = model.add_user(email, username, password, nationnality)
        if user_add==True :
            return render_template('user/signin.html')
    
    return render_template('user/signup.html')

@app.route("/signin", methods=['GET','POST'])
def signin():
    if request.method == 'POST' : 
        email = request.form['email'].strip()
        password = model.hash_psw(request.form['psw'])
        message = model.check_user_existence(email, password)
        if message == "ok" :
            session['id_user'] = model.get_user_from_email(email)[0]['id_user']
            session['email'] = email
            session['username'] = model.get_user_from_email(email)[0]['username']
            session['profile_picture'] = model.get_user_from_email(email)[0]['profile_picture']
            session['nationality'] = model.get_user_from_email(email)[0]['nationality']
            session['admin'] = model.get_user_from_email(email)[0]['admin']
            games_per_category = model.get_number_of_games_per_category()
            sessions_per_category = model.get_number_of_sessions_per_category()
            infos_categories = model.combine_infos_categories(games_per_category, sessions_per_category)
            return render_template('home.html', infos_categories=infos_categories)
        return render_template('user/signin.html', data=message)
    return render_template('user/signin.html')

@app.route('/logout')
def logout():
    session.pop('id_user', None)
    session.pop('email', None)
    session.pop('username', None)
    session.pop('profile_picture', None)
    session.pop('nationality', None)
    session.pop('admin', None)
    games_per_category = model.get_number_of_games_per_category()
    sessions_per_category = model.get_number_of_sessions_per_category()
    infos_categories = model.combine_infos_categories(games_per_category, sessions_per_category)
    return render_template('home.html', infos_categories=infos_categories)

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
    return render_template('admin/games/form_game.html', all_ctgs=ctgs)

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
    model.delete_one_game(id)
    print (id)
    return redirect("/admin_games", code=302)

# ---------------------------------------------------------------------------
# ---------------------------- Category
# ---------------------------------------------------------------------------

@app.route("/get_categories_from_game/<idGame>", methods=['GET', 'POST'])
def get_categories(idGame):
    data = model.get_categories_from_game_id(idGame)
    return data

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

@app.route("/categories/delete/<id>")
def delete_category(id):
    model.delete_category_from_id(id)
    return redirect("/admin_categories", code=302)


# ---------------------------------------------------------------------------
# ---------------------------- Session
# ---------------------------------------------------------------------------

@app.route("/session", methods=['GET', 'POST'])
def list_session():
    sessions = model.get_all_sessions()
    return render_template('session/session.html', sessions=sessions)

@app.route("/session/add", methods=['GET', 'POST'])
def add_session():
    if request.method == 'POST' :
        time = request.form['time']
        game = request.form['game']
        ctg = request.form['category']
        today = dt.today()
        user = session['id_user']
        model.add_new_session(time, today, game, user, ctg)
    games = model.get_all_games()
    return render_template('session/form_session.html', games=games)

@app.route("/session/delete/<id>")
def delete_session(id):
    model.delete_session_from_id(id)
    return redirect("/", code=302)



