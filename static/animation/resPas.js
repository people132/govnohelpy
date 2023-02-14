const form  = document.getElementsByTagName('form')[0];

const email = document.getElementById('email');
const emailError = document.querySelector('#email + span.error');
const newMail = document.getElementById('newMail');
const newMailError = document.querySelector('#newMail + span.error');
const password = document.getElementById('password');
const passwordError = document.querySelector('#password + span.error');
const passagain = document.getElementById('passagain');
const passagainError = document.querySelector('#passagain + span.error');

/*email.addEventListener('input', function (event) { // realtime валидатор
    if (email.validity.valid) { // почта
        emailError.textContent = '';
        emailError.className = 'error';
    } else {
        showErrorEmail()
    }
});
newMail.addEventListener('input', function (event) { // realtime валидатор
    if (newMail.validity.valid) { // почта Снова
        newMailError.textContent = '';
        newMailError.className = 'error';
    } else {
        showErrorNewMail()
    }
});
password.addEventListener('input', function (event) { // realtime валидатор
    if (password.validity.valid) { // пароль
        passwordError.textContent = '';
        passwordError.className = 'error';
    } else {
        showErrorPassword()
    }
});
passagain.addEventListener('input', function (event) { // realtime валидатор
    if(passagain.validity.valueMissing) { // пароль снова
        passagainError.textContent = 'Это обязательное поле';
        passagainError.className = 'error active';
    }
    else if(password.value != passagain.value) {
        passagainError.textContent = 'Пароли не соответствуют';
        passagainError.className = 'error active';
    }
    else {
        passagainError.textContent = '';
        passagainError.className = 'error';
    }
});
form.addEventListener('submit', function (event) { // Валидатор на кнопку
    if(!email.validity.valid) { // почта
        showErrorEmail()
        event.preventDefault();
    }
    if(!newMail.validity.valid) { // почта снова
        showErrorNewMail()
        event.preventDefault();
    }
    if(!password.validity.valid) { // пароль
        showErrorPassword()
        event.preventDefault();
    }
    if(passagain.validity.valueMissing) { // пароль снова
        passagainError.textContent = 'Это обязательное поле';
        passagainError.className = 'error active';
        event.preventDefault();
    }
    if(password.value != passagain.value) {
        passagainError.textContent = 'Пароли не соответствуют';
        passagainError.className = 'error active';
        event.preventDefault();
    }
});
function showErrorEmail() {
    if(email.validity.valueMissing) { // почта
        emailError.textContent = 'Это обязательное поле';
    } else if(email.validity.typeMismatch) {
        emailError.textContent = 'Это не похоже на почту';
    } else if(email.validity.tooShort) {
        emailError.textContent = `Почта должна содержать хотябы ${ email.minLength } символов. Вы ввели ${ email.value.length }.`;
    }
    emailError.className = 'error active';
}
function showErrorNewMail() {
    if(newMail.validity.valueMissing) { // почта снова
        newMailError.textContent = 'Это обязательное поле';
    } else if(newMail.validity.typeMismatch) {
        newMailError.textContent = 'Это не похоже на почту';
    } else if(newMail.validity.tooShort) {
        newMailError.textContent = `Почта должна содержать хотябы ${ newMail.minLength } символов. Вы ввели ${ newMail.value.length }.`;
    }
    newMailError.className = 'error active';
}
function showErrorPassword() {
    if(password.validity.valueMissing) { // пароль
        passwordError.textContent = 'Это обязательное поле';
    } else if(password.parentNode) {
        passwordError.textContent = 'Длина пароля должна быть от 8 до 30 символов, включать одну заглавную букву, один символ и одну цифру. Содержать только латинские буквы';
    }
    passwordError.className = 'error active';
}*/
var left_tab = document.getElementsByClassName("nav-link")[0];
var right_tab = document.getElementsByClassName("nav-link")[1];
left_tab.style["background-color"] = "#fff";
left_tab.style["color"] = "black";
right_tab.style["background-color"] = "#0260e8";
right_tab.style["color"] = "white";
left_tab.onclick = function(){
    left_tab.style["background-color"] = "#fff";
    left_tab.style["color"] = "black";
    right_tab.style["background-color"] = "#0260e8";
    right_tab.style["color"] = "white";
}
right_tab.onclick = function(){
    right_tab.style["background-color"] = "#fff";
    right_tab.style["color"] = "black";
    left_tab.style["background-color"] = "#0260e8";
    left_tab.style["color"] = "white";
}