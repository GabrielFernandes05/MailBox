import mongodb


def Main():
    while True:
        print(
            f"""
    1 - Cadastrar conta
    2 - Logar
    0 - Voltar
            """
        )
        op = input("Digite a opção: ")
        match op:
            case "1":
                CadastrarConta()
            case "2":
                logado_com = Logar()
                MenuLogar(logado_com)
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")


def MenuLogar(logado_com):
    while True:
        print(
            f"""
    1 - Alterar informações
    2 - Deletar conta
    0 - Voltar
            """
        )
        op = input("Digite a opção: ")
        match op:
            case "1":
                logado_com = AlterarInformações(logado_com)
            case "2":
                DeletarUsuario(logado_com)
                break
            case "0":
                print("Voltando...")
                break
            case _:
                print("Opção inválida.")


def CadastrarConta():
    while True:
        print(
            f"""
    1 - Cadastrar conta
    0 - Voltar
              """
        )
        op = input("Digite a opção: ")
        match op:
            case "1":
                lista_de_usuarios = []
                lista_de_ids = []
                mongodb.VerificarTodosOsUsuariosEJogarNaLista(
                    lista_de_usuarios, lista_de_ids, []
                )
                while True:
                    sucess = False
                    username = input("Digite o nome de usuário: ")
                    if username in lista_de_usuarios:
                        print("Usuário já cadastrado.")
                        continue
                    elif username == "":
                        print("Usuário não pode ser vazio.")
                        continue
                    elif username == "-1":
                        print("Voltando...")
                        break
                    elif len(username) < 3:
                        print("Usuário deve ter no mínimo 3 caracteres.")
                        continue
                    else:
                        sucess = True
                        break
                if sucess == True:
                    while True:
                        sucess = False
                        password = input("Digite a senha: ")
                        password2 = input("Digite a senha novamente: ")
                        if password != "-1" or password2 != "-1":
                            if password == password2:
                                sucess = True
                                break
                            else:
                                print("As senhas não são iguais.")
                        elif password == "-1" or password2 == "-1":
                            print("Voltando...")
                            break
                        else:
                            print("Opção inválida.")
                            continue
                    if sucess == True:
                        lista_de_ids.sort()
                        userid = lista_de_ids[-1] + 1
                        novo_usuario = [
                            {
                                "userid": userid,
                                "username": username,
                                "password": password,
                            }
                        ]
                        mongodb.InserirNovosUsuarios(novo_usuario)
                    else:
                        print("Voltando...")
                        break
                else:
                    break
            case "0":
                print("Voltando...")
                break
            case _:
                print("Opção inválida.")
                continue


def Logar():
    while True:
        print(
            f"""
    1 - Logar
    0 - Voltar
            """
        )
        op = input("Digite a opção: ")
        match op:
            case "1":
                lista_de_usuarios = []
                lista_de_senhas = []
                lista_de_ids = []
                mongodb.VerificarTodosOsUsuariosEJogarNaLista(
                    lista_de_usuarios, lista_de_ids, lista_de_senhas
                )
                while True:
                    logado_com_sucess = False
                    login = input("Digite o nome de usuário: ")
                    if login == "-1":
                        print("Voltando...")
                        break
                    elif login in lista_de_usuarios:
                        while True:
                            senha = input("Digite a senha: ")
                            if senha == "-1":
                                print("Voltando...")
                                break
                            elif senha in lista_de_senhas:
                                print("Logado com sucesso!")
                                logado_com = mongodb.ProcurarUmUsuarioPorUsername(login)
                                logado_com_sucess = True
                                return logado_com
                            else:
                                print("Senha incorreta.")
                        break
                    else:
                        print("Usuário não encontrado.")
                if logado_com_sucess == True:
                    break
            case "0":
                print("Voltando...")
                break
            case _:
                print("Opção inválida.")
                continue


def AlterarInformações(logado_com):
    if logado_com is not None:
        while True:
            print(
                f"""
    1 - Alterar nome de usuário
    2 - Alterar senha
    0 - Voltar
              """
            )
            op = input("Digite a opção: ")
            match op:
                case "1":
                    username1 = logado_com[0]["username"]
                    mongodb.VerificarTodosOsUsuariosEJogarNaLista(
                        lista_de_usuarios, [], lista_de_senhas
                    )
                    while True:
                        username = input("Digite o nome de usuário: ")
                        if username in lista_de_usuarios:
                            print("Usuário já cadastrado.")
                            continue
                        elif username == "":
                            print("Usuário não pode ser vazio.")
                            continue
                        elif username == "-1":
                            print("Voltando...")
                            break
                        elif len(username) < 3:
                            print("Usuário deve ter no mínimo 3 caracteres.")
                            continue
                        else:
                            break
                    mongodb.AtualizarUsername(username1, username)
                    logado_com[0]["username"] = username
                    return logado_com

                case "2":
                    password1 = logado_com[0]["password"]
                    while True:
                        password = input("Digite a senha: ")
                        password2 = input("Digite a senha novamente: ")
                        if password != "-1" or password2 != "-1":
                            if password == password2:
                                break
                            else:
                                print("As senhas não são iguais.")
                        elif password == "-1" or password2 == "-1":
                            print("Voltando...")
                            break
                        else:
                            print("Opção inválida.")
                            continue
                    mongodb.AtualizarSenha(password1, password2)
                    logado_com[0]["password"] = password2
                    return logado_com

                case "0":
                    print("Voltando...")
                    break


def DeletarUsuario(logado_com):
    if logado_com is not None:
        while True:
            print(
                f"""
    1 - Deletar conta
    0 - Voltar
                """
            )
            op = input("Digite a opção: ")
            match op:
                case "1":
                    while True:
                        confirmação = input(
                            f"Digite {logado_com[0]['username']} para confirmar: "
                        )
                        if confirmação == logado_com[0]["username"]:
                            mongodb.DeletarUsuario(logado_com[0]["username"])
                            print("Conta deletada com sucesso!")
                            logado_com = None
                            return logado_com
                        else:
                            print("Confirmação incorreta.")
                case "0":
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida.")
                    continue


Main()
