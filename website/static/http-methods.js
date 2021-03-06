/**
 * helper function to send a search query to the server
 */
$(function sendSearchQuery(){
    $("form[id=search]").submit(function(e) {
        e.preventDefault();
        const data = new FormData(e.target);
        const dataObj = Object.fromEntries(data.entries());
        var requestUrl = $(this).attr('action') + dataObj.search;
        $.ajax({
            url: requestUrl,
            type: 'GET',
            success: function(result){
                window.location.href = requestUrl
            }
        });
    });
});


/**
 * 
 * @param {*} requestUrl 
 * @param {*} requestType 
 */
function modCartQty(requestUrl, requestType){
    $.ajax({
        url: requestUrl,
        type: requestType,
        success: function(redirectUrl){
            window.location.href = redirectUrl
        }
    });
}


/**
 * helper function for sending put request. Get all the forms of this id and 
 * overrides their submit events
 */
$(function sendPutRequest(){
    $("form[id=put-form").each(function() { 
        $(this).submit(function(e) {
            e.preventDefault();
            const data = new FormData(e.target);
            const dataObj = Object.fromEntries(data.entries());
            var jsonForm = JSON.stringify(dataObj);
            var requestUrl = $(this).attr('action');
            $.ajax({
                url: requestUrl,
                type: 'PUT',
                contentType: "application/json",
                data: jsonForm,
                success: function(redirectUrl){
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