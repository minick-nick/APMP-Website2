// Navbar script that didn't work
$(document).ready(function() {
    $('.navbar-nav').on('click', 'a', function(){
        $('.navbar-nav a.active').removeClass('active');
        $(this).addClass('active');
    })
})
