import mongodb as mb


def Cadastrar(username, password, password2):
    lista_de_usuarios = []
    lista_de_ids = []
    mb.VerificarTodosOsUsuariosEJogarNaLista(lista_de_usuarios, lista_de_ids, [])
    if username not in lista_de_usuarios:
        if password == password2:
            lista_de_ids.sort()
            userid = lista_de_ids[-1] + 1
            novo_usuario = [
                {
                    "userid": userid,
                    "username": username,
                    "password": password,
                }
            ]
            mb.InserirNovosUsuarios(novo_usuario)
            return "Cadastrado com sucesso"
    else:
        return "Falha ao cadastrar, usuario ja existe ou senha invalida!"

def Login(username, password):
    lista_de_usuarios = []
    mb.VerificarTodosOsUsuariosEJogarNaLista(lista_de_usuarios, [], [])
    if username in lista_de_usuarios:
        usuario = mb.ProcurarUmUsuarioPorUsername(username)
        if password == usuario[0]["password"]:
            return "Logado com sucesso"
        else:
            return "Falha ao logar, senha incorreta!"
