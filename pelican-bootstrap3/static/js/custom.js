  $(document).ready(function(){
        $('div.cell div.prompt').hide(); // Hide jupyter cell numbers
  });

    var bigfoot = $.bigfoot(
        {
            deleteOnUnhover: false,
            preventPageScroll: false,
            hoverDelay: 250
        }
    );