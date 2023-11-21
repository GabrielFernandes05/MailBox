import pymongo
import sys
import datetime

try:
    client = pymongo.MongoClient(
        "mongodb+srv://gabrielfernandes05:yMNU5ztI2c7xuqsy@teste001.qzdzlzk.mongodb.net/?retryWrites=true&w=majority"
    )
except pymongo.errors.ConfigurationError:
    print(
        "An Invalid URI host error was received. Is your Atlas host name correct in your connection string?"
    )
    sys.exit(1)
db = client.ProjetoMailBox
my_collection = db["usuarios"]


def ReescreverUsuarios(novos_usuarios):
    try:
        my_collection.drop()
    except pymongo.errors.OperationFailure:
        print(
            "Um erro de autenticação foi recebido. Seu nome de usuário e senha estão corretos na string de conexão?"
        )
        sys.exit(1)
    try:
        result = my_collection.insert_many(novos_usuarios)
    except pymongo.errors.OperationFailure:
        print(
            "Um erro de autenticação foi recebido. Seu nome de usuário e senha estão corretos na string de conexão?"
        )
        sys.exit(1)
    else:
        inserted_count = len(result.inserted_ids)
        print(f"Foram inseridos {inserted_count} documentos.")


def InserirNovosUsuarios(novo_usuario):
    try:
        result = my_collection.insert_many(novo_usuario)
    except pymongo.errors.OperationFailure:
        print(
            "Um erro de autenticação foi recebido. Seu nome de usuário e senha estão corretos na string de conexão?"
        )
        sys.exit(1)
    else:
        inserted_count = len(result.inserted_ids)
        print(f"Usuario inserido com sucesso! {inserted_count} documentos.")


def DeletarUsuario(usuario):
    my_result = my_collection.delete_many({"$or": [{"username": usuario}]})
    print(f"Deletados {my_result.deleted_count} usuarios.")


def VerificarTodosOsUsuarios():
    result = my_collection.find()
    if result:
        c = 0
        for doc in result:
            userid = doc["userid"]
            c += 1
            username = doc["username"]
            password = doc["password"]
            print(f"{c}º - ID:{userid} - USUARIO:{username} - SENHA:{password}")
    else:
        print("No documents found.")


def VerificarTodosOsUsuariosEJogarNaLista(lista, ids, senhas):
    result = my_collection.find()
    if result:
        c = 0
        for doc in result:
            userid = doc["userid"]
            senha = doc["password"]
            username = doc["username"]
            lista.append(username)
            ids.append(userid)
            senhas.append(senha)
            c += 1
    else:
        print("No documents found.")


def VerificarMensagensDoUsuario(username):
    my_doc = my_collection.find_one({"username": username})
    if my_doc is not None:
        return my_doc["inbox"]
    else:
        print("Não achei nada")


def ProcurarUmUsuario(nome):
    my_doc = my_collection.find_one({"username": nome})

    if my_doc is not None:
        print(f"A senha do usuario {nome}:")
        print(my_doc["senha"])
    else:
        print("não achei nada")


def ProcurarUmUsuarioPorUsername(nome):
    my_doc = my_collection.find_one({"username": nome})

    if my_doc is not None:
        return [
            {
                "userid": my_doc["userid"],
                "username": my_doc["username"],
                "password": my_doc["password"],
            }
        ]
    else:
        print("não achei nada")


def ProcurarUmUsarioPorSenha(senha):
    my_doc = my_collection.find_one({"password": senha})

    if my_doc is not None:
        return [
            {
                "userid": my_doc["userid"],
                "username": my_doc["username"],
                "password": my_doc["password"],
            }
        ]
    else:
        print("não achei nada")


def AtualizarUsername(usuario_antigo, usuario_novo):
    my_doc = my_collection.find_one_and_update(
        {"username": usuario_antigo}, {"$set": {"username": usuario_novo}}, new=True
    )
    if my_doc is not None:
        print("Lista de usuarios atualizada:")
        print(my_doc["username"])
    else:
        print("Eu não achei nada")


def AdicionarMensagem(destino, msg):
    data_agora = str(datetime.datetime.now())
    msg.append(data_agora)
    my_doc = my_collection.find_one_and_update(
        {"username": destino}, {"$push": {"inbox": msg}}, new=True
    )


def AtualizarSenha(senha_antiga, senha_nova):
    my_doc = my_collection.find_one_and_update(
        {"password": senha_antiga}, {"$set": {"password": senha_nova}}, new=True
    )
    if my_doc is not None:
        print("Lista de usuarios atualizada:")
        print(my_doc["password"])
    else:
        print("Eu não achei nada")


def DeletarMensagem1(usuario, msg):
    mensagem = VerificarMensagensDoUsuario(usuario)
    print(mensagem)
    print(mensagem[0])
    for i in range(len(mensagem)):
        if mensagem[i] == msg:
            my_collection.update_one({"username": usuario}, {"$pull": {"inbox": msg}})
            print("Mensagem deletada")
