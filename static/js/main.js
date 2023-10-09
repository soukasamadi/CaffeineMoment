// Gets full year and display on the footer
$("#year").text(new Date().getFullYear());

// Back to the top button
$(".btt-link").click(function (e) {
    window.scrollTo(0, 0);
});

//Navbar background and color changes on scrooll
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(document).scrollTop() > 25) {
            $(".btt-button").addClass("back-top-active");
            $(".topnav").addClass("topnav-active");
        } else {
            $(".btt-button").removeClass("back-top-active");
            $(".topnav").removeCla
ss("topnav-active");
        }
    });
});


//Contact Form ajax
$(document).on("submit", "#contact-form-ajax", function (e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: "/ajax_contact_form",
        data: {
        "name": $('#name').val(),
        "email": $('#email').val(),
        "message": $('#message').val(),
        },
        success: function () {
            console.log("sent success!");
        },
    });
});



