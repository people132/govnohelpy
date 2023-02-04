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
document.getElementsByClassName("tablet")[1].style.height = "11.25vw";
var flag = 0;
var tablet_history = document.getElementsByClassName("tablet")[1];
var tablet_orders = document.getElementsByClassName("tablet")[0];
document.getElementById("tablet_of_CO_arrow_frame").onclick = function() {
    if(flag === 0){
        if (window.innerWidth <= 454){
            tablet_history.style['border-radius'] = '25px 25px 4px 25px';    
        }
        for (let i = 2; i < 8; i++) {
            document.getElementsByTagName("tr")[6 + i].style.display = "";
        }
        Changename("tablet_of_CO_arrow_frame", "↑")
        checkForChanges();
        setTimeout(() => {  document.getElementById("arrow_left_frame").classList.add('b-show') }, 1000);
        setTimeout(() => {  document.getElementById("arrow_left_frame").style.display = "flex"; }, 1000);
        setTimeout(() => {  document.getElementById("arrow_right_frame").classList.add('b-show') }, 1000);
        setTimeout(() => {  document.getElementById("arrow_right_frame").style.display = "flex"; }, 1000);
        setTimeout(() => {  document.getElementById("counter").classList.add('b-show') }, 1000);
        setTimeout(() => {  document.getElementById("counter").style.display = "flex"; }, 1000);
        checkForChanges();
        flag = 1;
    }
    else{
        tablet_history.style['border-radius'] = '25px';
        for (let i = 2; i < 8; i++) {
            document.getElementsByTagName("tr")[6 + i].style.display = "none";
        }
        Changename("tablet_of_CO_arrow_frame", "↓")
        document.getElementById("arrow_left_frame").style.display = "none";
        document.getElementById("arrow_right_frame").style.display = "none";
        document.getElementById("counter").style.display = "none";
        checkForChanges();
        flag = 0
    }

    return false;
  };

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
let tablet_left = document.getElementsByClassName("tablet_of_CO_el_left");
let tablet_right = document.getElementsByClassName("tablet_of_CO_el_right");
for (let i = 0; i < 8; i++) {
    tablet_left[i].textContent = history[i][0];
    tablet_right[i].textContent = history[i][1];
}

var page = 0;
document.getElementById("arrow_right_frame").onclick = function() {
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
document.getElementById("arrow_left_frame").onclick = function() {
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

tablet_history.style.top = "320px";
var checkForChanges = function() {
    //относительно верхней таблицы
    var hth = tablet_orders.offsetHeight;
    var tth = tablet_orders.offsetTop;
    document.getElementById("container1").style.top = 100 + hth + tth + "px";

     //относительно нижней таблицы
    var hth = tablet_history.offsetHeight;
    var tth = tablet_history.offsetTop;
    document.getElementById("tablet_of_CO_arrow_frame").style.top = (tth + hth - 1 )+ "px";
    document.getElementById("arrow_left_frame").style.top = (tth + hth - 1) + "px";
    document.getElementById("arrow_right_frame").style.top = (tth + hth - 1) + "px";
    document.getElementById("counter").style.top = (tth + hth - 1) + "px";
    document.getElementsByTagName("footer")[0].style.top = (200 + tth + hth) + "px";

    //подгоним высоту таблички с заработком под высоту таблицы с заказами
    if (window.innerWidth > 1071){  
        var earnedCircle = document.getElementsByClassName("earned_circle_tablet")[0];
        earnedCircle.style['height'] = tablet_orders.offsetHeight + "px";
    }
    else {
        var earnedCircle = document.getElementsByClassName("earned_circle_tablet")[0];
        earnedCircle.style['height'] = "22.5vw";
    }

};
checkForChanges();
new ResizeObserver(checkForChanges).observe(tablet_history);
