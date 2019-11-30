window.addEventListener('DOMContentLoaded', (event) => {
    jQuery('.navFixa').css("background-color", "");
    jQuery(window).scroll(function() {
        if (jQuery(window).scrollTop() > 10) {
            jQuery('.navFixa').css("background-color", "#0E1122");
            jQuery('.navFixa a:hover').css("");
        } else {
            jQuery('.navFixa').css("background-color", "");
            jQuery('.navFixa a:hover').css("");
        }
    });
});

function busca(event){
    if(event.key === "Enter"){
    }
}