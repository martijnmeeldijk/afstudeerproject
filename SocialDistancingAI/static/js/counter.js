jQuery(function ($) {
    setInterval(update_numbers, 5000);
    update_numbers();
    function update_numbers(){
        $.get( "/get-people", function( data ) {
            $("#people").text(data);
          });
        $.get( "/get-violations", function( data ) {
            $("#violations").text(data);
          });
    }
    
});