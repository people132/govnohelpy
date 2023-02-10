function Changename(fieldName, text) {
    fieldName = document.getElementById(fieldName);
    fieldName.textContent = text;
}
let history = [ ["видеомонтаж. fiverr. свадебный ролик. (хронометраж) 1ч20мин. 13 700р. до 29.10", "9800 (1.12 в 7:23)"], 
                ["1", "1"], 
                ["2", "2"], 
                ["3", "3"], 
                ["4", "4"], 
                ["5", "5"], /*твой массив*/
                ["6", "6"], 
                ["7", "7"], 
                ["8555523423415fsdg", "84234"], 
                ["9", "9"], 
                ["10", "10"], 
                ["11", "11"], 
                ["12", "12"],
                ["13", "13"],
                ["14", "14"],
                ["15", "15"],
                ["16", "16"],
                ["17", "17"],
                ["18", "18"],
                ["19", "19"],
                ["20", "20"] ];


var tablet_history = document.getElementsByClassName("tablet")[1];
var flag = 0;

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
}

for (let i = 2; i < 8; i++) {
    document.getElementsByTagName("tr")[6 + i].style.display = "none";
}
for (let i = 0; i < 8; i++) {
    tablet_history.rows[i + 1].cells[0].textContent = history[i][0];
    tablet_history.rows[i + 1].cells[1].textContent = history[i][1];
}

var page = 0;
document.getElementsByClassName("arrow_page_frame")[1].onclick = function() {
    if(history.length > (page + 1) * 8){
        page++;
        Changename("counter", (page + 1).toString());
        for (let i = 0; i < 8; i++) {
            if(page * 8 + i + 1 <= history.length){
                tablet_history.rows[i + 1].cells[0].textContent = history[page * 8 + i][0];
                tablet_history.rows[i + 1].cells[1].textContent = history[page * 8 + i][1];
            }
            else{
                tablet_history.rows[i + 1].cells[0].textContent = "";
                tablet_history.rows[i + 1].cells[1].textContent = "";
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
                tablet_history.rows[i + 1].cells[0].textContent = history[page * 8 + i][0];
                tablet_history.rows[i + 1].cells[1].textContent = history[page * 8 + i][1];
            }
            else{
                tablet_history.rows[i + 1].cells[0].textContent = "";
                tablet_history.rows[i + 1].cells[1].textContent = "";
            }
        }
    } 
}
