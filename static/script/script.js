let login_usuario = window.document.getElementById("logininput");
let senha_usuario = window.document.getElementById("senhainput");
let login_usuario_cadastro = window.document.getElementById("logincadastro");
let senha_usuario_cadastro = window.document.getElementById("senhacadastro");
let senha_usuario_cadastro_confirmar = window.document.getElementById("senhacadastroconfirmar");

let usuarios_cadastrados = {
    "adm": "123a",
    "user": "123a"
};

function Cadastrar() {
    if (login_usuario_cadastro.value in usuarios_cadastrados) {
        window.alert("usuario existente!")
    } else {
        if (senha_usuario_cadastro.value === senha_usuario_cadastro_confirmar.value) {
            usuarios_cadastrados[login_usuario_cadastro.value] = senha_usuario_cadastro.value;
            login_usuario_cadastro.value = "";
            senha_usuario_cadastro.value = "";
            senha_usuario_cadastro_confirmar.value = "";
            console.log(usuarios_cadastrados);
        } else {
            window.alert("senhas não são iguais");

        };

    };
};

function Logar() {
    if (login_usuario.value in usuarios_cadastrados) {
        if (usuarios_cadastrados[login_usuario.value] === senha_usuario.value) {
            window.location.href = "main.html";
        } else {
            window.alert("Senha não cadastrada neste usuario!")
            console.log(usuarios_cadastrados[login_usuario.value])
        }
    } else {
        window.alert("Usuario não cadastrado!")
    }
};

function Cadastrar2() {
    let novo_usuario = {
        username: login_usuario_cadastro.value,
        password: senha_usuario_cadastro.value,
    };
    login_usuario_cadastro.value = "";
    senha_usuario_cadastro.value = "";
    senha_usuario_cadastro_confirmar.value = "";
    return novo_usuario;
}

let usuario_para_cadastrar = Cadastrar2();