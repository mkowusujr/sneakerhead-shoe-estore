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

function addColor(requestUrl){
    var form = addForm(requestUrl, "POST");
    var newColor = document.createElement("input");
    newColor.setAttribute("type", "text");
    newColor.setAttribute("name", "color");
    newColor.setAttribute("placeholder", "enter color");
    form.appendChild(newColor);

    var submit = document.createElement("input");
    submit.setAttribute("type", "submit");
    submit.setAttribute("value", "add color");
    form.appendChild(submit);

    document.getElementById("colors").appendChild(form);
}

function addSize(requestUrl){
    form = addForm(requestUrl, "POST");
    var newSize = document.createElement("input");
    newSize.setAttribute("type", "number");
    newSize.setAttribute("name", "size");
    newSize.setAttribute("placeholder", "enter size");
    newSize.setAttribute("min", "0");
    form.appendChild(newSize);

    var sizeQuantity = document.createElement("input");
    sizeQuantity.setAttribute("type", "number");
    sizeQuantity.setAttribute("name", "quantity");
    sizeQuantity.setAttribute("placeholder", "enter quantity");
    sizeQuantity.setAttribute("min", "0");
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

function navToggle(){
    let navbarLinks = document.getElementsByClassName('nav-links')[0];
    if (navbarLinks.style.display === "block") {
        navbarLinks.style.display = "none";
        document.body.style.overflowY = 'visible';
        window.onscroll = function() {};
    } else {
        navbarLinks.style.display = "block";
        document.body.style.overflowY = "hidden";
        window.onscroll = () => { window.scroll(0, 0); };
    }
}

let widthMatch = window.matchMedia("(min-width: 1221px)");
widthMatch.addEventListener('change', function(mm) {
    let navbarLinks = document.getElementsByClassName('nav-links')[0];
    if (mm.matches) {
        navbarLinks.style.display = "block";
    }
    else {
        navbarLinks.style.display = "none";
    }
});