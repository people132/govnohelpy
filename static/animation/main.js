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
    var tooltip = document.getElementsByClassName("tooltip")[0];
    var tooltip_title = document.getElementsByClassName("tooltip_title")[0];
    var tooltip_main_text = document.getElementsByClassName("tooltip_main_text")[0];
    document.getElementsByClassName("close")[0].onclick = function(){
        tooltip.classList.remove("_active");
    }
    document.getElementsByClassName("row_button")[0].onclick = function(){
        tooltip_title.textContent = "Преодоление языкового барьера";
        tooltip_main_text.textContent = "Для общения с иностранными заказчиками недостаточно переводчика в браузере. Мы будем вести переговоры с заказчиками за вас, соблюдая вежливость и ваши интересы.";
        tooltip.classList.add("_active");
    }
    document.getElementsByClassName("row_button")[1].onclick = function(){
        tooltip_title.textContent = "Поиск и проверка заказов";
        tooltip_main_text.textContent = "Все заказы будут взяты с проверенных зарубежных источников. В личном кабинете вы можете указать стоит ли предлагать вам заказы только с зарубежных платформ";
        tooltip.classList.add("_active");
    }
    document.getElementsByClassName("row_button")[2].onclick = function(){
        tooltip_title.textContent = "Помощь с оформлением платежных систем";
        tooltip_main_text.textContent = "Мы полностью проконсультируем вас по регистрации платёжных систем и пройдём вместе с вами путь от получения гонорара на платформе до зачисления его на ваш счёт";
        tooltip.classList.add("_active");
    }
    document.getElementsByClassName("row_button")[3].onclick = function(){
        tooltip_title.textContent = "Оформление аккаунта";
        tooltip_main_text.textContent = "Каждая фриланс-биржа требует правильное оформление аккаунта, полное описание ваших навыков на иностранном языке. Иначе, ваш профиль будет на последних строчках в поиске, что означает меньше просмотров и заказов. Мы оформим аккаунт за вас или предложим конкретный план действий, ориентированный конкретно под вашу деятельность.";
        tooltip.classList.add("_active");
    }
}

document.getElementsByClassName("a_footer")[3].onclick = function() {
    location.href='/number';
};
document.getElementsByClassName("a_footer")[4].onclick = function() {
    location.href='/mail';
};