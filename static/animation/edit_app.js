var select_for_menagers = document.getElementById('menagers');
for (i = 0; i < 9; i++) {
    var option = document.createElement('option');
    option.value = option.innerHTML = i;
    select_for_menagers.appendChild(option);
 }