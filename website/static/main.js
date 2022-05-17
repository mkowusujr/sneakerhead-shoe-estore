/**
 * helper function that uses jquery ajax to send a delete request to the server
 * @param {*} url 
 */
function sendDelete(url){
    $.ajax({
        url: url,
        type: 'DELETE',
        success: function(result){
            window.location.href = "/inventory"
        }
    });
}


/**
 * helper function for sending put request
 */
$(document).ready(function(){
    $('form[id=put-form]').submit(function(e) {
        e.preventDefault();
        const data = new FormData(e.target);
        const value = Object.fromEntries(data.entries());
        var jsonForm = JSON.stringify(value)
        $.ajax({
            url: $("form[id=put-form]").attr('action'),
            type: 'PUT',
            contentType: "application/json",
            data: jsonForm,
            success: function(result){
                window.location.href = "/inventory"
            }
        });
    });
});