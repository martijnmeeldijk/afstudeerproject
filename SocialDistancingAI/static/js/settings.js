const url = 'http://localhost:5000/get-config';
let form = $('.form');




$(document).ready(function () {
   load_form();
});

function load_form(){
    $.getJSON(url, function (data) {
        form.empty();
        $.each(data, function (key, entry) {
            form.append(
                $(`
                <div class="row">
                <div class="col-md-6">
                <div class="input-group mb-3">
                <input type="text" class="form-control" id="${key}" value="${key}" disabled>
                </div>
                </div>
                <div class="col-md-6">
                <div class="input-group mb-3">
                <input type="text" class="form-control" id="${entry}" value="${entry}" >
                <div class="input-group-append">
                <button type="button" onclick="submit_button('${key}', '${entry}')" style="margin: 0 !important" class="btn btn-outline-primary">submit</button>
                </div>
                </div>
                </div>
                
                </div>
                
                `));
        });

    });
}

function submit_button(key, value){

    val = $(`#${value}`).val();

    $.get( `/set-config/${key}/${val}`, function( data ) {
        console.log(data);
        load_form();
      });
}