from flask import Flask,request,render_template,redirect, session
from flask_cors import CORS
from datetime import date as dt
from werkzeug.utils import secure_filename
import model
import os


app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')
CORS(app)

app.config['UPLOAD_FOLDER_USERS'] = 'static/img/users/'
app.config['UPLOAD_FOLDER_GAMES'] = 'static/img/games/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 

# Crée les répertoires d'images si pas déjà créés
if not os.path.exists(app.config['UPLOAD_FOLDER_USERS']):
    os.makedirs(app.config['UPLOAD_FOLDER_USERS'])
if not os.path.exists(app.config['UPLOAD_FOLDER_GAMES']):
    os.makedirs(app.config['UPLOAD_FOLDER_GAMES'])

@app.route("/")
def index():
    games_per_category = model.get_number_of_games_per_category()
    sessions_per_category = model.get_number_of_sessions_per_category()
    infos_categories = model.combine_infos_categories(games_per_category, sessions_per_category)
    return render_template('home.html', infos_categories=infos_categories)

@app.route("/search", methods=['GET'])
def search():
    if request.method == 'GET':
        game_name = request.args.get('games-search')
        games = model.search_games_by_name(game_name)
        return render_template('game/games.html', games=games)
    return

# ---------------------------------------------------------------------------
# ---------------------------- Admin
# ---------------------------------------------------------------------------

@app.route("/admin_games")
def admin_games():
    if 'admin' in session and session['admin']==1 : 
        data = model.get_all_games()
        return render_template('admin/games/admin_games.html', games=data)
    return redirect ("/", code=302)

@app.route("/admin_categories")
def admin_categories():
    if 'admin' in session and session['admin']==1 : 
        data = model.get_all_category()
        return render_template('admin/categories/admin_categories.html', categories=data)
    return redirect ("/", code=302)

@app.route("/admin_sessions")
def admin_sessions():
    if 'admin' in session and session['admin']==1 : 
        sessions = model.get_all_sessions()
        return render_template('admin/sessions/admin_sessions.html', sessions=sessions)
    return redirect ("/", code=302)

@app.route("/admin_users")
def admin_users():
    if 'admin' in session and session['admin']==1 :
        data = model.get_all_users()
        return render_template('admin/users/admin_users.html', users = data)
    return redirect ("/", code=302)

# ---------------------------------------------------------------------------
# ---------------------------- Users
# ---------------------------------------------------------------------------
   
@app.route("/users/<id>", methods=['GET']) 
def user(id):
    data = model.get_user(int(id))
    if 'id_user' in session :
        if session['admin']==0 :
            if session['id_user']==int(id):   
                return render_template('profile.html', user=data)
            return redirect ("/", code=302)
        return render_template('profile.html', user=data)
    return redirect ("/", code=302)

@app.route("/user/edit/<id>", methods=['GET', 'POST'])
def edit_user(id):
    if 'admin' in session and session['admin']==1 :  
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


            #Enregistrement de l'image
            if 'image' not in request.files:
                return 'No file part'
            file = request.files['image']
            if file and model.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER_USERS'], filename)
                file.save(file_path)
                model.save_user_image_to_db(filename, id)
                session['profile_picture_name'] = filename
                

            return redirect("/users/" + str(session['admin']), code=302)
        data = model.get_user(int(id))
        return render_template('user/edit_user.html', user=data)
    return redirect ("/", code=302)


@app.route("/user/delete/<id>", methods=['GET', 'POST'])
def delete_user(id):
    if 'admin' in session and session['admin']==1 :  
        model.delete_one_user(int(id))
        return redirect("/admin_users", code=302)
    return redirect ("/", code=302)

# ---------------------------------------------------------------------------
# ---------------------------- Connexion/Inscription/Comptes
# ---------------------------------------------------------------------------

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
            session['profile_picture_name'] = model.get_user_from_email(email)[0]['profile_picture_name']
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
    session.pop('profile_picture_name', None)
    session.pop('nationality', None)
    session.pop('admin', None)
    return redirect ("/", code=302)

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
    ctgs = model.get_categories_from_game_id(id)
    return render_template('game/game.html', game=data, ctgs=ctgs)

@app.route("/games/add", methods=['GET', 'POST'])
def add_game():
    if 'admin' in session and session['admin']==1 :      
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


            # Enregistrement de l'image
            if 'image' not in request.files:
                return 'No file part'
            file = request.files['image']
            if file and model.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER_GAMES'], filename)
                file.save(file_path)
                model.save_game_image_to_db(filename, id_new_game)


        ctgs = model.get_all_category()
        return render_template('admin/games/form_game.html', all_ctgs=ctgs)
    return redirect ("/", code=302)

@app.route("/games/edit/<id>", methods=['GET', 'POST'])
def edit_game(id):
    if 'admin' in session and session['admin']==1 : 
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


            # Enregistrement de l'image
            if 'image' not in request.files:
                return 'No file part'
            file = request.files['image']
            if file and model.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER_GAMES'], filename)
                file.save(file_path)
                model.save_game_image_to_db(filename, id_new_game)


        data = model.get_game(int(id))
        ctgs = model.get_all_category()
        game_ctgs = model.get_categories_from_game_id(int(id))
        # game_ctgs = [ctg['id_category'] for ctg in game_ctgs]
        return render_template('admin/games/form_game.html', game=data, all_ctgs=ctgs, game_ctgs=game_ctgs)
    return redirect ("/", code=302)

@app.route("/games/delete/<id>", methods=['GET', 'POST'])
def delete_game(id):
    if 'admin' in session and session['admin']==1 : 
        model.delete_one_game(id)
        print (id)
        return redirect("/admin_games", code=302)
    return redirect ("/", code=302)

@app.route("/get_session_from_game_category", methods=['GET'])
def get_session_from_game_and_category():
    if request.method == 'GET':
        id_game = request.args.get('id_game')
        id_ctg = request.args.get('id_ctg')
        sessions = model.get_session_from_game_category(id_game, id_ctg)
        return sessions
    return

# ---------------------------------------------------------------------------
# ---------------------------- Category
# ---------------------------------------------------------------------------

@app.route("/get_categories_from_game/<idGame>", methods=['GET', 'POST'])
def get_categories(idGame):
    data = model.get_categories_from_game_id(idGame)
    return data

@app.route("/category/add", methods=['GET', 'POST'])
def add_category():
    if 'admin' in session and session['admin']==1 : 
        if request.method == 'POST':
            label = request.form.get('label').strip()
            description = request.form.get('description').strip()
            model.add_new_category(label,description)
        return render_template('admin/categories/form_category.html')
    return redirect ("/", code=302)

@app.route("/categories/edit/<id>", methods=['GET', 'POST'])
def edit_category(id):
    if 'admin' in session and session['admin']==1 : 
        if request.method == 'POST':
            label = request.form.get('label').strip()
            description = request.form.get('description').strip()
            model.update_category(id,label,description)
            data = model.get_all_category()
            return render_template('admin/categories/admin_categories.html', categories=data)
        category = model.get_category_from_id(id)
        return render_template('admin/categories/form_category.html', ctg=category)
    return redirect ("/", code=302)

@app.route("/categories/delete/<id>")
def delete_category(id):
    if 'admin' in session and session['admin']==1 : 
        model.delete_category_from_id(id)
        return redirect("/admin_categories", code=302)
    return redirect ("/", code=302)


# ---------------------------------------------------------------------------
# ---------------------------- Session
# ---------------------------------------------------------------------------

@app.route("/sessions", methods=['GET', 'POST'])
def get_sessions_of_user():
    sessions = model.get_sessions_from_user(int(session['id_user']))
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
        sessions = model.get_all_sessions()
        return render_template('session/session.html', sessions=sessions)
    games = model.get_all_games()
    return render_template('session/form_session.html', games=games)

@app.route("/session/delete/<id>")
def delete_session(id):
    model.delete_session_from_id(id)
    return redirect("/admin_sessions", code=302)



