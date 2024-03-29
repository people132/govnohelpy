const form  = document.getElementsByTagName('form')[0]; // форма для смены ПОЧТЫ!!

const email = document.getElementById('email');
const emailError = document.querySelector('#email + span.error');
const newMail = document.getElementById('newMail');
const newMailError = document.querySelector('#newMail + span.error');
const password = document.getElementById('passwordMail');
const passwordError = document.querySelector('#passwordMail + span.error');

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

/*document.getElementsByClassName("nav-link")[0].onclick = function() {
    window.location = ("resPas");
};*/

