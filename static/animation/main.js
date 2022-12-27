console.log("ПРИВ");

const animItems = document.querySelectorAll(".anim_items");
console.log(animItems.length);
if(animItems.length > 0){
    window.addEventListener("scroll", animOnScroll);
    function animOnScroll(){
        for(let i = 0; i < animItems.length; i++){
            const animItem = animItems[i];
            const animItemHeight = animItem.offsetHeight;
            const animItemOffset = offset(animItem).top;
            const animStart = 4;
            
            let animItemPointer = window.innerHeight - animItemHeight / animStart;
            if(animItemHeight > window.innerHeight){
                animItemPointer = window.innerHeight - window.innerHeight / animStart;
            }

            if ((window.pageYOffset > (animItemOffset - animItemPointer)) && (window.pageYOffset < (animItemOffset + animItemHeight))){
                animItem.classList.add("_active");
            }
        }
    }
    function offset(el) {
        var rect = el.getBoundingClientRect(),
        scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
        scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        return { top: rect.top + scrollTop, left: rect.left + scrollLeft }
    }
    animOnScroll();
}

function Changename(fieldName, text) {
    fieldName = document.getElementById(fieldName);
    fieldName.textContent = text;
}

function ChangeURL(fieldName, URL){
    fieldName = document.getElementById(fieldName);
    fieldName.href = URL;
}
var flag = 0;
document.getElementById("tablet_of_CO_arrow_frame").onclick = function() {
    if(flag === 0){
        document.getElementsByClassName("tablet_of_CO")[0].style.height = "410px";
        document.getElementById("tablet_of_CO_arrow_frame").style.top = "calc(130% + 205px)";
        Changename("tablet_of_CO_arrow_frame", "↑")
        document.getElementsByTagName("footer")[0].style.top = "180%";
        flag = 1;
    }
    else{
        document.getElementsByClassName("tablet_of_CO")[0].style.height = "205px";
        document.getElementById("tablet_of_CO_arrow_frame").style.top = "calc(130%)";
        Changename("tablet_of_CO_arrow_frame", "↓")
        document.getElementsByTagName("footer")[0].style.top = "150%";
        flag = 0
    }

    return false;
  };
