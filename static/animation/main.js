console.log("ПРИВ");

const animItems = document.querySelectorAll(".anim_items");
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


    function adaptiveFunc() {
        var w = window.innerWidth;
        if (w <= 805) {
            document.getElementsByClassName("how_we_works_block")[1].style["margin-right"] = "0";
            document.getElementsByClassName("how_we_works_block")[1].style["margin-left"] = "0";
            document.getElementsByClassName("how_we_works_block")[1].style["margin-top"] = "max(80px, 4.17vw)";
            document.getElementsByClassName("how_we_works_block")[2].style["margin-top"] = "max(80px, 4.17vw)";
            document.getElementsByClassName("break")[10].style["display"] = "block";
            document.getElementsByClassName("break")[11].style["display"] = "block";
        }
        else if (w > 805 && w <= 1265) {
            document.getElementsByClassName("how_we_works_block")[1].style["margin-right"] = "0";
            document.getElementsByClassName("how_we_works_block")[1].style["margin-left"] = "max(80px, 4.17vw)";
            document.getElementsByClassName("how_we_works_block")[1].style["margin-top"] = "0";
            document.getElementsByClassName("how_we_works_block")[2].style["margin-top"] = "max(80px, 4.17vw)";
            document.getElementsByClassName("break")[10].style["display"] = "none";
            document.getElementsByClassName("break")[11].style["display"] = "block";
        }
        else{
            document.getElementsByClassName("how_we_works_block")[1].style["margin-right"] = "max(80px, 4.17vw)";
            document.getElementsByClassName("how_we_works_block")[1].style["margin-left"] = "max(80px, 4.17vw)";
            document.getElementsByClassName("how_we_works_block")[1].style["margin-top"] = "0";
            document.getElementsByClassName("how_we_works_block")[2].style["margin-top"] = "0";
            document.getElementsByClassName("break")[10].style["display"] = "none";
            document.getElementsByClassName("break")[11].style["display"] = "none";
        }
    }
    window.addEventListener('resize', function() {
        adaptiveFunc();
    });
    adaptiveFunc();
}