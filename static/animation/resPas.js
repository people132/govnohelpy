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

/*document.getElementsByClassName("nav-link")[1].onclick = function() {
    window.location = ("resMail");
};*/