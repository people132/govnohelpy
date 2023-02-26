if(window.location.href == 'http://127.0.0.1:5000/re'){
    window.location.replace(window.location.href + "#Pas");
}
const form  = document.getElementsByTagName('form')[1]; // форма для смены ПОЧТЫ!!

const email = document.getElementById('email');
const emailError = document.querySelector('#email + span.error');
const newMail = document.getElementById('newMail');
const newMailError = document.querySelector('#newMail + span.error');
const password = document.getElementById('password');
const passwordError = document.querySelector('#password + span.error');
const passagain = document.getElementById('passagain');
const passagainError = document.querySelector('#passagain + span.error');

email.addEventListener('input', function (event) { // realtime валидатор
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
}

const Pform  = document.getElementsByTagName('form')[0]; // форма для смены ПАРОЛЯ!!

const Pemail = document.getElementById('Pemail');
const PemailError = document.querySelector('#Pemail + span.error');
const Ppassword = document.getElementById('Ppassword');
const PpasswordError = document.querySelector('#Ppassword + span.error');
const newPassword = document.getElementById('newPassword');
const newPasswordError = document.querySelector('#newPassword + span.error');
const newPassagain = document.getElementById('newPassagain');
const newPassagainError = document.querySelector('#newPassagain + span.error');

Pemail.addEventListener('input', function (event) { // realtime валидатор
    if (Pemail.validity.valid) { // почта
        PemailError.textContent = '';
        PemailError.className = 'error';
    } else {
        showErrorPemail()
    }
});
Ppassword.addEventListener('input', function (event) { // realtime валидатор
    if (Ppassword.validity.valid) { // пароль
        PpasswordError.textContent = '';
        PpasswordError.className = 'error';
    } else {
        showErrorPpassword()
    }
});
newPassword.addEventListener('input', function (event) { // realtime валидатор
    if (newPassword.validity.valid) { // новый пароль
        newPasswordError.textContent = '';
        newPasswordError.className = 'error';
    } else {
        showErrorNewPassword()
    }
});
newPassagain.addEventListener('input', function (event) { // realtime валидатор
    if(newPassagain.validity.valueMissing) { // новый пароль снова
        newPassagainError.textContent = 'Это обязательное поле';
        newPassagainError.className = 'error active';
    }
    else if(newPassword.value != newPassagain.value) {
        newPassagainError.textContent = 'Пароли не соответствуют';
        newPassagainError.className = 'error active';
    }
    else {
        newPassagainError.textContent = '';
        newPassagainError.className = 'error';
    }
});
Pform.addEventListener('submit', function (event) { // Валидатор на кнопку
    if(!Pemail.validity.valid) { // почта
        showErrorPemail()
        event.preventDefault();
    }
    if(!Ppassword.validity.valid) { // пароль
        showErrorPpassword()
        event.preventDefault();
    }
    if(!newPassword.validity.valid) { // пароль
        showErrorNewPassword()
        event.preventDefault();
    }
    if(newPassagain.validity.valueMissing) { // пароль снова
        newPassagainError.textContent = 'Это обязательное поле';
        newPassagainError.className = 'error active';
        event.preventDefault();
    }
    if(newPassword.value != newPassagain.value) {
        newPassagainError.textContent = 'Пароли не соответствуют';
        newPassagainError.className = 'error active';
        event.preventDefault();
    }
});
function showErrorPemail() {
    if(Pemail.validity.valueMissing) { // почта
        PemailError.textContent = 'Это обязательное поле';
    } else if(Pemail.validity.typeMismatch) {
        PemailError.textContent = 'Это не похоже на почту';
    } else if(Pemail.validity.tooShort) {
        PemailError.textContent = `Почта должна содержать хотябы ${ Pemail.minLength } символов. Вы ввели ${ Pemail.value.length }.`;
    }
    PemailError.className = 'error active';
}
function showErrorPpassword() {
    if(Ppassword.validity.valueMissing) { // пароль
        PpasswordError.textContent = 'Это обязательное поле';
    } else if(Ppassword.parentNode) {
        PpasswordError.textContent = 'Длина пароля должна быть от 8 до 30 символов, включать одну заглавную букву, один символ и одну цифру. Содержать только латинские буквы';
    }
    PpasswordError.className = 'error active';
}
function showErrorNewPassword(){
    if(newPassword.validity.valueMissing) { // пароль
        newPasswordError.textContent = 'Это обязательное поле';
    } else if(newPassword.parentNode) {
        newPasswordError.textContent = 'Длина пароля должна быть от 8 до 30 символов, включать одну заглавную букву, один символ и одну цифру. Содержать только латинские буквы';
    }
    newPasswordError.className = 'error active';
}




var left_tab = document.getElementsByClassName("nav-link")[0];
var right_tab = document.getElementsByClassName("nav-link")[1];
left_tab.classList.add("active_tab");
right_tab.classList.remove("active_tab");
left_tab.onclick = function(){
    left_tab.classList.add("active_tab");
    right_tab.classList.remove("active_tab");
    document.getElementsByClassName("head")[0].textContent = "Изменение пароля";
}
right_tab.onclick = function(){
    right_tab.classList.add("active_tab");
    left_tab.classList.remove("active_tab");
    document.getElementsByClassName("head")[0].textContent = "Изменение почты";
}