const form  = document.getElementsByTagName('form')[0];

const email = document.getElementById('email');
const emailError = document.querySelector('#email + span.error');
const password = document.getElementById('password');
const passwordError = document.querySelector('#password + span.error');
const passagain = document.getElementById('passagain');
const passagainError = document.querySelector('#passagain + span.error');
const number = document.getElementById('number');
const numberError = document.querySelector('#number + span.error');
const username = document.getElementById('username');
const usernameError = document.querySelector('#username + span.error');
const surname = document.getElementById('surname');
const surnameError = document.querySelector('#surname + span.error');
const patronymic = document.getElementById('patronymic');
const patronymicError = document.querySelector('#patronymic + span.error');

email.addEventListener('input', function (event) { // realtime валидатор
    if (email.validity.valid) { // почта
        emailError.textContent = '';
        emailError.className = 'error';
    } else {
        showErrorEmail()
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
number.addEventListener('input', function (event) { // realtime валидатор
    if (number.validity.valid) { // номер
        numberError.textContent = '';
        numberError.className = 'error';
    } else {
        showErrorNumber()
    }
});
username.addEventListener('input', function (event) { // realtime валидатор
    if (username.validity.valid) { // Имя
        usernameError.textContent = '';
        usernameError.className = 'error';
    } else {
        showErrorUsername()
    }
});
surname.addEventListener('input', function (event) { // realtime валидатор
    if (surname.validity.valid) { // Фамилия
        surnameError.textContent = '';
        surnameError.className = 'error';
    } else {
        showErrorSurname()
    }
});
patronymic.addEventListener('input', function (event) { // realtime валидатор
    if (patronymic.validity.valid) { // Фамилия
        patronymicError.textContent = '';
        patronymicError.className = 'error';
    } else {
        showErrorPatronymic()
    }
});


form.addEventListener('submit', function (event) { // Валидатор на кнопку
    if(!email.validity.valid) { // почта
        showErrorEmail()
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
    if(!number.validity.valid) { // номер
        showErrorNumber()
        event.preventDefault();
    }
    if(!username.validity.valid) { // Имя
        showErrorUsername()
        event.preventDefault();
    }
    if(!surname.validity.valid) { // Фамилия
        showErrorSurname()
        event.preventDefault();
    }
    if(!patronymic.validity.valid) { // Отчество
        showErrorPatronymic()
        event.preventDefault();
    }
    // отправляем форму
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
function showErrorPassword() {
    if(password.validity.valueMissing) { // пароль
        passwordError.textContent = 'Это обязательное поле';
    } else if(password.parentNode) {
        passwordError.textContent = 'Длина пароля должна быть от 8 до 30 символов, включать одну заглавную букву, один символ и одну цифру. Содержать только латинские буквы';
    }
    passwordError.className = 'error active';
}
function showErrorNumber() {
    if(number.validity.valueMissing) { // номер
        numberError.textContent = 'Это обязательное поле';
    } else if(number.parentNode) {
        numberError.textContent = 'Введён некорректный номер';
    }
    numberError.className = 'error active';
}
function showErrorUsername() {
    if(username.validity.valueMissing) { // Имя
        usernameError.textContent = 'Это обязательное поле';
    } else if (username.validity.tooShort) {
        usernameError.textContent = `Длина имени должна быть от ${ username.minLength } символов. Вы ввели ${ username.value.length }.`;
    } else if(username.parentNode) {
        usernameError.textContent = 'Имя должно содержать только буквы';
    }
    usernameError.className = 'error active';
}
function showErrorSurname() {
    if(surname.validity.valueMissing) { // Фамилия
        surnameError.textContent = 'Это обязательное поле';
    } else if (surname.validity.tooShort) {
        surnameError.textContent = `Длина фамилии должна быть от ${ surname.minLength } символов. Вы ввели ${ surname.value.length }.`;
    } else if(surname.parentNode) {
        surnameError.textContent = 'Фамилия должна содержать только буквы';
    }
    surnameError.className = 'error active';
}
function showErrorPatronymic() {
    if(patronymic.validity.valueMissing) { // Фамилия
        patronymicError.textContent = 'Это обязательное поле';
    } else if (patronymic.validity.tooShort) {
        patronymicError.textContent = `Длина фамилии должна быть от ${ patronymic.minLength } символов. Вы ввели ${ patronymic.value.length }.`;
    } else if(patronymic.parentNode) {
        patronymicError.textContent = 'Фамилия должна содержать только буквы';
    }
    patronymicError.className = 'error active';
}

function onSubmit(token) {
    form.submit();
}
