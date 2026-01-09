// Variáveis devem estar declaradas dentro da função pra não dar erro no carregamento
const passInput = document.querySelector('input[name="password"]')
const passBT = document.querySelector('#showPass')
function showPass(){
    if (passInput.type === 'password'){ // Verifica se o TIPO, NÃO VALOR, é igual a password (lembre-se de que é um input)
        passInput.type = 'text'
        // passInput.type === 'text } Precisa usar um setAtributte para alterar algo'
    } else{
        passInput.type = 'password';
    }
}
passBT.addEventListener("click", showPass)