from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)


# Define routes for login and signup
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
