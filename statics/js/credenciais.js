function displayInputs(value){
    chave_privada = document.getElementsByClassName('field-chave_privada')[0]
    usuario = document.getElementsByClassName('field-usuario')[0]
    senha = document.getElementsByClassName('field-senha')[0]
    
    if(value == 'usuario_senha'){
        chave_privada.style.display = 'none'
        usuario.style.display = 'block'
        senha.style.display = 'block'
    }else if(value == 'chave_privada'){
        chave_privada.style.display = 'block'
        usuario.style.display = 'none'
        senha.style.display = 'none'
    }else{
        chave_privada.style.display = 'block'
        usuario.style.display = 'block'
        senha.style.display = 'block'
    }
}

document.addEventListener('DOMContentLoaded', (event) => {
    var senha = document.getElementsByName('senha')[0]
    senha.type = 'password'
    
    var tipo_credenciais = document.getElementsByName('tipo_credencial')[0]
    displayInputs(tipo_credenciais.value)
    tipo_credenciais.addEventListener('change',(event) => {
        displayInputs(tipo_credenciais.value)
    }) 
})

