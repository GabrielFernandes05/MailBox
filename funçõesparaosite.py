import mongodb

def Cadastrar(username, password, password2):
    lista_de_usuarios = []
    lista_de_ids = []
    mongodb.VerificarTodosOsUsuariosEJogarNaLista(
        lista_de_usuarios, lista_de_ids, []
    )
    if username not in lista_de_usuarios:
        if password == password2:
            lista_de_ids.sort()
            userid = lista_de_ids[-1] + 1
            mongodb.InserirUsuario(userid, username, password)
            return "Cadastrado com sucesso"
    else:
        return "Falha ao cadastrar, usuario ja existe ou senha invalida!"