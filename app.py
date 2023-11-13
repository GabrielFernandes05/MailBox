from flask import Flask, render_template, request, redirect, url_for, flash, session
import funçõesparaosite as fps

app = Flask(__name__)
app.secret_key = "KJ4g5k2j5G2k4j5G2KJ4g5k2J5G2k4j5gK2J4g"


@app.route("/submitcadastro", methods=["POST"])
def submitcadastro():
    username = request.form["username"]
    password = request.form["password1"]
    password2 = request.form["password2"]
    fps.Cadastrar(username, password, password2)
    return redirect(url_for("login"))


@app.route("/submitlogin", methods=["GET", "POST"])
def submitlogin():
    username1 = request.form["username"]
    password = request.form["password"]
    login_result = fps.Login(username1, password)
    if login_result == "Logado com sucesso":
        session["username"] = username1
        return redirect(url_for("user_page", username=username1))
    else:
        return login_result


@app.route("/mandarmensagem", methods=["GET", "POST"])
def mandarmensagem():
    usuario = session.get("username")
    destino = request.form.get("selectmensagem")
    mensagem = request.form.get("mensagem")
    fps.MandarMensagem(usuario, mensagem, destino)
    print(f"mensagem:{mensagem}, destino:{destino}, usuario:{usuario}")
    return redirect(url_for("user_page", username=usuario))


@app.route("/user_page")
def user_page():
    username = request.args.get("username")
    return render_template("user_page.html", username=username)


@app.route("/atualizar_lista", methods=["GET", "POST"])
def atualizar_lista():
    lista_de_usuarios = fps.ListaDeTodosOsUsuarios()
    username = session.get("username")
    return render_template("user_page.html", lista=lista_de_usuarios, username=username)


@app.route("/deslogar")
def deslogar():
    session.pop("username", None)
    return redirect(url_for("login"))


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
