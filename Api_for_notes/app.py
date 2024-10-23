from flask import Flask, render_template, url_for, request, redirect, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from models import db, User, Note
from forms import LoginForm, RegisterForm, NoteForm
from flask_bcrypt import Bcrypt
from sqlalchemy import text

#####
# Pogrubienie, pochylenie, zmiana rozmiaru czcionki, zmiana koloru czcionki, podkreślenie (przyciskami)
# Możliwość wyeksportowania notatki do jakiegoś pliku 
#####

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Own_projects/Api_for_notes/test.db'
app.config['SECRET_KEY'] = 'testsecretkey'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template("index.html")
 
@app.route("/login", methods=['Get', 'Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("notes", username=current_user.username))
    return render_template("login.html", form=form)

@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/register", methods=['Get', 'Post'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("register.html", form=form)

@app.route(f"/notes/<username>", methods=['Get', 'Post'])
@login_required
def notes(username):
    form = NoteForm()

    notes_list = Note.query.filter_by(user_id=current_user.id).all()
    note = None

    if form.validate_on_submit():
        new_note = Note(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('notes', username=current_user.username))

    return render_template("notes.html", form=form, notes=notes_list, note=note)

@app.route(f"/load_note/<note_id>", methods=['Get', 'Post'])
@login_required
def load_note(note_id):
    form = NoteForm()
    
    note = Note.query.get_or_404(note_id)
    notes_list = Note.query.filter_by(user_id=current_user.id).all()

    if note.user_id != current_user.id:
        flash("You don't have permission for this note!", "danger")
        return redirect(url_for("notes", username=current_user.username))
    
    if form.validate_on_submit():
        # update_note = Note(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.execute(text(f"UPDATE note SET title='{form.title.data}', content='{form.content.data}', user_id={current_user.id} WHERE id={note_id}"))
        db.session.commit()
        return redirect(url_for('notes', username=current_user.username))

    return render_template("notes.html", form=form, notes=notes_list, note=note)

if __name__ == "__main__":
    app.run(debug=True)
