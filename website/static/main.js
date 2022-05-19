function redirectUrl(url){
    window.location.href = url;
}

function addForm(requestUrl, method){
    // create form
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", requestUrl);
    return form
}

function addSize(requestUrl){
    form = addForm(requestUrl, "POST");
    var newSize = document.createElement("input");
    newSize.setAttribute("type", "number");
    newSize.setAttribute("name", "size");
    newSize.setAttribute("placeholder", "enter size");
    form.appendChild(newSize);

    var sizeQuantity = document.createElement("input");
    sizeQuantity.setAttribute("type", "number");
    sizeQuantity.setAttribute("name", "quantity");
    sizeQuantity.setAttribute("placeholder", "enter quantity");
    form.appendChild(sizeQuantity);

    var submit = document.createElement("input");
    submit.setAttribute("type", "submit");
    submit.setAttribute("value", "add size");
    form.appendChild(submit);

    // var header = document.createElement("h3");
    // header.innerText("Enter the Info");
    // // header.textContent("Enter the Info")
    // document.getElementById("quantities").appendChild(header);
    
    document.getElementById("quantities").appendChild(form);
}