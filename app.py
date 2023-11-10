from flask import Flask, render_template, request, redirect, url_for, flash
import funçõesparaosite as fps


app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    fps.Cadastrar(username, password, password2)
    return redirect(url_for('login'))

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/")
def inicio():
    return redirect(url_for("cadastro"))


if __name__ == "__main__":
    app.run(debug=True)
