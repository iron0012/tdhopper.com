$(document).ready(function() {
    $('div.cell div.prompt').hide(); // Hide jupyter cell numbers

    var bigfoot = $.bigfoot({
        deleteOnUnhover: false,
        preventPageScroll: false,
        hoverDelay: 250
    });

    /*============================================
    Project thumbs - Masonry
    ==============================================*/
    $(window).load(function() {

        $('#projects-container').css({
            visibility: 'visible'
        });

        $('#projects-container').masonry({
            itemSelector: '.project-item:not(.filtered)',
            columnWidth: 320,
            isFitWidth: true,
            isResizable: true,
            isAnimated: !Modernizr.csstransitions,
            gutterWidth: 25
        });

        scrollSpyRefresh();
        waypointsRefresh();
    });

    /*============================================
    Filter Projects
    ==============================================*/
    $('#filter-works a').click(function(e) {
        e.preventDefault();

        $('#filter-works li').removeClass('active');
        $(this).parent('li').addClass('active');

        var category = $(this).attr('data-filter');

        $('.project-item').each(function() {
            if ($(this).is(category)) {
                $(this).removeClass('filtered');
            } else {
                $(this).addClass('filtered');
            }

            $('#projects-container').masonry('reload');
        });

        scrollSpyRefresh();
        waypointsRefresh();
    });



});