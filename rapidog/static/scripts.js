window.addEventListener('DOMContentLoaded', (event) => {
    jQuery('.layout-navbar').css("background-color", "");
    jQuery(window).scroll(function() {
        if (jQuery(window).scrollTop() > 10) {
            jQuery('.layout-navbar').css("background-color", "#0E1122");
            jQuery('.layout-navbar a:hover').css("");
        } else {
            jQuery('.layout-navbar').css("background-color", "");
            jQuery('.layout-navbar a:hover').css("");
        }
    });
});

let botao = document.querySelector('.refresh');
botao.onclick = function refresh(){
    window.history.back();
}

function dropdown() {
    document.getElementById("dropdown").classList.toggle("mostrar");
}
  
window.onclick = function(event) {
    if (!event.target.matches('.botao-drop')) {
    let dropdown = document.getElementById("dropdown");
        if (dropdown.classList.contains('mostrar')) {
            dropdown.classList.remove('mostrar');
        }
    }
}
