var total_violations = 0

jQuery(function ($) {
    setInterval(update_numbers, 1000);
    update_numbers();
    function update_numbers(){
        $.get( "/get-people", function( data ) {
            $("#people").text(data);
          });
      
        $.get( "/get-total-violations", function( data ) {
          if(data != total_violations){
            total_violations = data
            $("#violations-triangle").css('color', 'red');
            $("#violations-triangle").removeClass('fa-tachometer-alt-slowest').addClass('fa-tachometer-alt-fastest')
          }
          else{
            $("#violations-triangle").css('color', 'green');
            $("#violations-triangle").removeClass('fa-tachometer-alt-fastest').addClass('fa-tachometer-alt-slowest')
          }

          $("#total-violations").text(data);
        });
    }
    
});