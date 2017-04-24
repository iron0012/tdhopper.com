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

    /*============================================
    Tooltips
    ==============================================*/
    $("[data-toggle='tooltip']").tooltip();

    /*============================================
    Placeholder Detection
    ==============================================*/
    if (!Modernizr.input.placeholder) {
        $('#contact-form').addClass('no-placeholder');
    }

    /*============================================
    Scrolling Animations
    ==============================================*/
    $('.scrollimation').waypoint(function(){
        $(this).addClass('in');
    },{offset:function(){
            var h = $(window).height();
            var elemh = $(this).outerHeight();
            if ( elemh > h*0.3){
                return h*0.7;
            }else{
                return h - elemh;
            }
        }
    });

    /*============================================
    Resize Functions
    ==============================================*/
    $(window).resize(function(){
        scrollSpyRefresh();
        waypointsRefresh();
    });
    /*============================================
    Refresh scrollSpy function
    ==============================================*/
    function scrollSpyRefresh(){
        setTimeout(function(){
            $('body').scrollspy('refresh');
        },1000);
    };

    /*============================================
    Refresh waypoints function
    ==============================================*/
    function waypointsRefresh(){
        setTimeout(function(){
            $.waypoints('refresh');
        },1000);
    };


    /*============================================
    ScrollTo Links
    ==============================================*/
    $('a.scrollto').click(function(e){
        $('html,body').scrollTo(this.hash, this.hash, {gap:{y:-50},animation:  {easing: 'easeInOutCubic', duration: 1600}});
        e.preventDefault();

        if ($('.navbar-collapse').hasClass('in')){
            $('.navbar-collapse').removeClass('in').addClass('collapse');
        }
    });

});