from flask import Flask, render_template, request, redirect, url_for, flash
import funçõesparaosite as fps


app = Flask(__name__)


@app.route("/submitcadastro", methods=["POST"])
def submitcadastro():
    username = request.form["username"]
    password = request.form["password1"]
    password2 = request.form["password2"]
    fps.Cadastrar(username, password, password2)
    return redirect(url_for("login"))

@app.route("/submitlogin", methods=["POST"])
def submitlogin():
    username = request.form["username"]
    password = request.form["password"]
    fps.Login(username, password)
    return redirect(url_for("inicio"))


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
