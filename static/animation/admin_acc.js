function Changename(fieldName, text) {
    fieldName = document.getElementById(fieldName);
    fieldName.textContent = text;
}
for (let i = 2; i < 8; i++) {
    document.getElementsByTagName("tr")[15 + i].style.display = "none";
}

var flag = 0;
var tablet_history = document.getElementsByClassName("tablet")[1];
var tablet_orders = document.getElementsByClassName("tablet")[0];

document.getElementById("tablet_of_CO_arrow_frame").onclick = function() {
    if(flag === 0){
        for (let i = 2; i < 8; i++) {
            document.getElementsByTagName("tr")[15 + i].style.display = "";
        }
        Changename("tablet_of_CO_arrow_frame", "↑");
        document.getElementById("arrow_block").style.display = "flex";
        flag = 1;
    }
    else{
        for (let i = 2; i < 8; i++) {
            document.getElementsByTagName("tr")[15 + i].style.display = "none";
        }
        Changename("tablet_of_CO_arrow_frame", "↓")
        document.getElementById("arrow_block").style.display = "none";
        flag = 0;
    }

    return false;
};

function loadJSON(path, success)
{
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function()
    {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                if (success)
                    success(JSON.parse(xhr.responseText));
            } 
        }
    };
    xhr.open("GET", path, true);
    xhr.send();
}
let flag_drop = 0;

function show_dropdown(x){
    const drop = x.previousElementSibling;
    if(!flag_drop){
        x.textContent = "Закрыть"
        x.parentNode.style["border-radius"] = "max(1.3vw, 25px) max(1.3vw, 25px) 0 0";
        drop.classList.add("show_drop");
        flag_drop = 1;
    }
    else{
        x.textContent = "Сменить статус"
        x.parentNode.style["border-radius"] = "max(1.3vw, 25px)";
        drop.classList.remove("show_drop");
        flag_drop = 0;
    }

}


