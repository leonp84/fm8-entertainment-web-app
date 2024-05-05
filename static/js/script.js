$(function (){
    $('.movie').hover(function() {
        $(this).children('.play-button').toggle();
    });

    $('.play-button').hover(function() {
        $('.play-button').toggleClass('play-hover')
    });

    $('.bookmark-icon').hover(function() {
        $(this).toggleClass('bookmark-hover');
        $(this).find('path').toggleClass('bookmark-hover');
    });

    $('.bookmark-icon').on('click', function() {
        $(this).find('path').toggleClass('bookmarked-clicked');
    });


});