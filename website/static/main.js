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