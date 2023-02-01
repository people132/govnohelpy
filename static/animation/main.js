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
}