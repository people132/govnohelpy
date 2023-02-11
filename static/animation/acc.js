function Changename(fieldName, text) {
    fieldName = document.getElementById(fieldName);
    fieldName.textContent = text;
}

function ChangeURL(fieldName, URL){
    fieldName = document.getElementById(fieldName);
    fieldName.href = URL;
}
for (let i = 2; i < 8; i++) {
    document.getElementsByTagName("tr")[6 + i].style.display = "none";
}
var flag = 0;
var tablet_history = document.getElementsByClassName("tablet")[1];
var tablet_orders = document.getElementsByClassName("tablet")[0];
document.getElementById("tablet_of_CO_arrow_frame").onclick = function() {
    if(flag === 0){
        for (let i = 2; i < 8; i++) {
            document.getElementsByTagName("tr")[6 + i].style.display = "";
        }
        Changename("tablet_of_CO_arrow_frame", "↑");
        document.getElementById("arrow_block").style.display = "flex";
        flag = 1;
    }
    else{
        for (let i = 2; i < 8; i++) {
            document.getElementsByTagName("tr")[6 + i].style.display = "none";
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
loadJSON('../static/animation/temp1.json',
    function(data) { 
        let history = data[document.getElementById("email").textContent];
        let tablet_left = document.getElementsByClassName("tablet_of_CO_el_left");
        let tablet_right = document.getElementsByClassName("tablet_of_CO_el_right");
        for (let i = 0; i < 8; i++) {
            tablet_left[i].textContent = history[i][0];
            tablet_right[i].textContent = history[i][1];
        }

        var page = 0;
        document.getElementsByClassName("arrow_page_frame")[1].onclick = function() {
            if(history.length > (page + 1) * 8){
                page++;
                Changename("counter", (page + 1).toString());
                for (let i = 0; i < 8; i++) {
                    if(page * 8 + i + 1 <= history.length){
                        tablet_left[i].textContent = history[page * 8 + i][0];
                        tablet_right[i].textContent = history[page * 8 + i][1];
                    }
                    else{
                        tablet_left[i].textContent = "";
                        tablet_right[i].textContent = "";
                    }
                }
            }
        }
        document.getElementsByClassName("arrow_page_frame")[0].onclick = function() {
            if(page > 0){
                page--;
                Changename("counter", (page + 1).toString());
                for (let i = 0; i < 8; i++) {
                    if(page * 8 + i + 1 < history.length){
                        tablet_left[i].textContent = history[page * 8 + i][0];
                        tablet_right[i].textContent = history[page * 8 + i][1];
                    }
                    else{
                        tablet_left[i].textContent = "";
                        tablet_right[i].textContent = "";
                    }
                }
            } 
        }
    },
);
