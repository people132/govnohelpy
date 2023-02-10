document.getElementsByClassName("btn_pozvol")[0].onclick = function() {
    var password = document.getElementById('password');
    var passagain = document.getElementById('passagain');
    if(password.value != passagain.value){
        passagain.style["border-color"] = "rgb(206, 4, 4)";
        passagain.style["box-shadow"] = "0.32vw 0.27vw 0.78vw 0px rgba(255, 1, 1, 0.3)";
    }
    else {
        passagain.style["border-color"] = "rgba(21, 232, 2, 0.712)";
        passagain.style["box-shadow"] = "0.32vw 0.27vw 0.78vw 0px rgba(2, 168, 16, 0.575)";
    }
}