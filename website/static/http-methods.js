/**
 * helper function for sending put request. Get all the forms of this id and 
 * overrides their submit events
 */
$(function sendPutRequest(){
    $("form[id=put-form").each(function() { 
        $(this).submit(function(e) {
            e.preventDefault();
            const data = new FormData(e.target);
            const value = Object.fromEntries(data.entries());
            var jsonForm = JSON.stringify(value)
            var requestUrl = $(this).attr('action')
            $.ajax({
                url: requestUrl,
                type: 'PUT',
                contentType: "application/json",
                data: jsonForm,
                success: function(redirectUrl){
                    // alert(result)
                    window.location.href = redirectUrl
                }
            });
        });
    });
});

/**
 * helper function that uses jquery ajax to send a delete request to the server
 * @param {*} requestUrl the request url being sent to the server
 */
function sendDeleteRequest(requestUrl){
    $.ajax({
        url: requestUrl,
        type: 'DELETE',
        success: function(redirectUrl){
            window.location.href = redirectUrl
        }
    });
}