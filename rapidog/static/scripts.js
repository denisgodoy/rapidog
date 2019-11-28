window.addEventListener('DOMContentLoaded', (event) => {
    jQuery('.navFixa').css("background-color", "");
    jQuery(window).scroll(function() {
        if (jQuery(window).scrollTop() > 10) {
            jQuery('.navFixa').css("background-color", "#0E1122");
            jQuery('.navFixa a').css("color", "white");            
        } else {
            jQuery('.navFixa').css("background-color", "");
            jQuery('.navFixa a').css("color", "white"); 
        }
    });
});

// function mouseOver() {
//     document.getElementById("produto").style.backgroundColor = "rgb(245, 245, 245)";
//   }
  
//   function mouseOut() {
//     document.getElementById("produto").style.backgroundColor = "white";
//   }

// document.getElementById("produto").onmouseover = function() {mouseOver()};
// document.getElementById("produto").onmouseout = function() {mouseOut()};