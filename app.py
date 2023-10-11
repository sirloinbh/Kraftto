from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# Define your User model here (with SQLAlchemy).


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


# Define routes for login and signup
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Implement user authentication logic here (validate username and password).
        # If authentication succeeds, create a JWT and return it to the user.
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify(message="Invalid credentials"), 401
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Implement user registration logic here (create a new user).
        username = request.form.get('password')
        password = request.form.get('username')

        print('hello')

        hashed_password = bcrypt.generate_password_hash(
            password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)



        db.session.commit()

        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')


if __name__ == '__main__':
    with app.app_context() : 
        db.create_all()


    app.run(debug=True)

