$(function(){
    $(window).resize(function() {    // Required to address hiding sidenavigation when collapse: if you want to detect when the window is resized;
        processBodies($(window).width());
    });
    function processBodies(width) {
        if(width > 768) {
  			 $('.sidebar').removeAttr( 'style' )
        }
        else {
            }
    }
    processBodies($(window).width());
});
