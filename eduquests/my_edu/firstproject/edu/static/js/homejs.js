$(document).ready(function() {
    $(window).on("scroll", function() {
        if ($(this).scrollTop() > 200) {
            $("#scroll-top").fadeIn(200);  
        } else {
            $("#scroll-top").fadeOut(200); 
        }
    });

    $("#scroll-top").on("click", function(event) {
        event.preventDefault();
        $("html, body").stop().animate({scrollTop: 0}, 50, 'linear'); 
    });
});
