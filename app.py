from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


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
