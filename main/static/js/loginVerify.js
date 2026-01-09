const loginBt = document.querySelector('.login-bt')

function validateFields(){
    // Variáveis criadas a fim de facilitar a compreensão e design do sistema
    const isEmailValid = validateEmail();
    const isPasswordValid = validatePassword();

    loginBt.disabled = !(isEmailValid && isPasswordValid); 
}
// Verifica se o e-mail é uma string
function isEmail(email){
    return /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email);
}
// Executa a função anterior usando o valor inserido pelo usuário
function validateEmail(){
    const email = document.querySelector('input[name="email"]').value;
    if (!email){
        return false
    } else{
        return isEmail(email);
    }
}
// Verifica se o valor da senha possui um determinado comprimento.
function validatePassword(){
    const pasw = document.querySelector('input[name="password"]').value;
    return pasw.length >= 8;
}