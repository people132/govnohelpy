const form  = document.getElementsByTagName('form')[0];

const username = document.getElementById('username');
const usernameError = document.querySelector('#username + span.error');
const surname = document.getElementById('surname');
const surnameError = document.querySelector('#surname + span.error');
const patronymic = document.getElementById('patronymic');
const patronymicError = document.querySelector('#patronymic + span.error');
const number = document.getElementById('number');
const numberError = document.querySelector('#number + span.error');

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
});
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

document.getElementsByClassName("a_footer")[3].onclick = function() {
    location.href='/number';
};
document.getElementsByClassName("a_footer")[4].onclick = function() {
    location.href='/mail';
};