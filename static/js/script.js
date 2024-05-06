$(function (){

    if ($(window).width() > 1000) {
    $('.item').hover(function() {
        $(this).children('.play-button').toggle();
    });

    $('.play-button').hover(function() {
        $('.play-button').toggleClass('play-hover');
    });

    $('.bookmark-icon').hover(function() {
        $(this).toggleClass('bookmark-hover');
        $(this).find('path').toggleClass('bookmark-hover');
    });
    }
    
    $(".bookmark-icon").click(function() {
        if ($(this).find('path').attr('fill') == 'none') {

        } else {
            $(this).find('path').attr('fill', 'none');
            $(this).find('path').attr('stroke', 'white');
            $(this).find('path').attr('stroke-width', '1.5');

        } 
        // console.log($(this).find('.item-id').text())
        $.ajax({
            url: "/update_bookmarks/",
            type: "POST",
            dataType: "json",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": CSRF_TOKEN, 
                'item': $(this).find('.item-id').text()
              },
            success: function(response) {
                console.log(response.message);
            },
            error: function(xhr, status, error) {
                console.error("Error:", error);
            }
        });
    });

});