jQuery(function ($) {
    setInterval(update_numbers, 1000);
    update_numbers();
    function update_numbers(){
        $.get( "/get-people", function( data ) {
            $("#people").text(data);
          });
        $.get( "/get-violations", function( data ) {
            $("#violations").text(data);
          });
        $.get( "/get-total-violations", function( data ) {
          $("#total-violations").text(data);
        });
    }
    
});