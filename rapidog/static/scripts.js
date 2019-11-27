window.addEventListener('DOMContentLoaded', (event) => {
    // jQuery('.navFixa').css("background-color", "rgba(255, 255, 255, 0.2)");
    jQuery('.navFixa').css("background-color", "");
    jQuery(window).scroll(function() {
        if (jQuery(window).scrollTop() > 10) {
            jQuery('.navFixa').css("background-color", "white");
            jQuery('.navFixa a').css("color", "#0E1122");            
        } else {
            // jQuery('.navFixa').css("background-color", "rgba(255, 255, 255, 0.2)");
            jQuery('.navFixa').css("background-color", "");
            jQuery('.navFixa a').css("color", "white"); 
        }
    });
});