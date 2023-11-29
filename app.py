from flask import Flask, render_template, request, redirect, url_for, flash, session
import funçõesparaosite as fps
import mongodb as mb

app = Flask(__name__)
app.secret_key = "KJ4g5k2j5G2k4j5G2KJ4g5k2J5G2k4j5gK2J4g"


# Pagina inicial
@app.route("/")
def inicio():
    return redirect(url_for("cadastro"))


# Pagina de cadastro
@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/submitcadastro", methods=["POST"])
def submitcadastro():
    username = request.form["username"]
    password = request.form["password1"]
    password2 = request.form["password2"]
    fps.Cadastrar(username, password, password2)
    return redirect(url_for("login"))


# Pagina de login
@app.route("/login")
def login():
    return render_template("login.html")


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


# Pagina de usuario
@app.route("/user_page")
def user_page():
    username = request.args.get("username")
    return render_template("user_page.html", username=username)


@app.route("/deslogar")
def deslogar():
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/configs")
def configs():
    username = session.get("username")
    return render_template("configs.html", username=username)


@app.route("/atualizar_lista", methods=["GET", "POST"])
def atualizar_lista():
    lista_de_usuarios = fps.ListaDeTodosOsUsuarios()
    username = session.get("username")
    return render_template("user_page.html", lista=lista_de_usuarios, username=username)


@app.route("/mandarmensagem", methods=["GET", "POST"])
def mandarmensagem():
    usuario = session.get("username")
    destino = request.form.get("selectmensagem")
    mensagem = request.form.get("mensagem")
    fps.MandarMensagem(usuario, mensagem, destino)
    print(f"mensagem:{mensagem}, destino:{destino}, usuario:{usuario}")
    return redirect(url_for("user_page", username=usuario))


@app.route("/deletarmensagens", methods=["GET", "POST"])
def deletarmensagens():
    username = session.get("username")
    mensagens_selecionadas = request.form.getlist("mensagem")
    mensagens = mb.VerificarMensagensDoUsuario(username)
    for c in mensagens_selecionadas:
        mb.DeletarMensagem1(username, c)
        print("Mensagem deletada")
    return render_template(
        "user_page.html",
        mensagens_selecionadas=mensagens_selecionadas,
        mensagens=mensagens,
        username=username,
    )


# Pagina de configurações
@app.route("/voltarparauserpage")
def voltarparauserpage():
    username = session.get("username")
    return redirect(url_for("user_page", username=username))


@app.route("/mudarnomedeusuario", methods=["POST"])
def mudarnomedeusuario():
    username = session.get("username")
    print(username)
    novo_username = request.form["novousername"]
    print(novo_username)
    senha = request.form["passwordmudaruser"]
    print(senha)
    lista_de_usuarios = []
    lista_de_senhas = []
    mb.VerificarTodosOsUsuariosEJogarNaLista(lista_de_usuarios, [], lista_de_senhas)
    print(lista_de_usuarios)
    print(lista_de_senhas)
    if novo_username in lista_de_usuarios:
        print("Esse nome de usuário já existe")
    else:
        print("Esse nome de usuário não existe")
    if senha in lista_de_senhas:
        print("Essa senha existe")
    else:
        print("Essa senha não existe")
    if novo_username == username or novo_username in lista_de_usuarios:
        return "Esse nome de usuário já existe"
    else:
        senha_do_usuario = mb.VerificarSenhadeUmUsuario(username)
        if senha == senha_do_usuario:
            mb.AtualizarUsername(username, novo_username)
            session["username"] = novo_username
            return redirect(url_for("user_page", username=novo_username))
        else:
            return "Senha incorreta"
    return redirect(url_for("configs", username=username))


@app.route("/mudarsenhadeusuario", methods=["GET", "POST"])
def mudarsenhadeusuario():
    username = session.get("username")
    print(username)
    senha1 = request.form["password1"]
    print(senha1)
    senha2 = request.form["password2"]
    print(senha2)
    senha_atual = request.form["passwordmudarsenha"]
    print(senha_atual)
    if senha1 == senha2:
        if senha1 == senha_atual and senha2 == senha_atual:
            return "A nova senha não pode ser igual a senha atual"
        else:
            senha_do_usuario = mb.VerificarSenhadeUmUsuario(username)
            if senha_atual == senha_do_usuario:
                mb.AtualizarSenha(username, senha1)
                return redirect(url_for("user_page", username=username))
            else:
                return "Senha incorreta"
    else:
        return "As senhas não são iguais"
    return redirect(url_for("configs", username=username))


@app.route("/deletarusuario", methods=["GET", "POST"])
def deletarconta():
    username = session.get("username")
    senha = request.form["passworddeletarconta"]
    senha_do_usuario = mb.VerificarSenhadeUmUsuario(username)
    if senha == senha_do_usuario:
        mb.DeletarUsuario(username)
        return redirect(url_for("cadastro"))
    else:
        return "Senha incorreta"
    return redirect(url_for("configs", username=username))


if __name__ == "__main__":
    app.run(debug=True)
