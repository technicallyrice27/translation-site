$(window).load( function() {

    if (sessionStorage.getItem('forTheme')) {
        var theme1 = document.getElementById("forTheme");
        theme1.className = sessionStorage.getItem('forTheme');
    }
    if (sessionStorage.getItem('divTheme')) {
        var theme2 = document.getElementById("divTheme");
        theme2.className = sessionStorage.getItem('divTheme');
    }
});

$(document).ready( function() {

    $("#swapColors").click( function(event) {
        sessionStorage.clear();
       var divElement = document.querySelector("#forTheme");
       divElement.classList.toggle("light-theme");
       divElement.classList.toggle("dark-theme");
       sessionStorage.setItem('forTheme', divElement.classList);
       var divElement = document.querySelector("#divTheme");
       divElement.classList.toggle("light-theme");
       divElement.classList.toggle("dark-theme");
       sessionStorage.setItem('divTheme', divElement.classList);
    });

    $("#swapColorsMobile").click( function(event) {
        sessionStorage.clear();
       var divElement = document.querySelector("#forTheme");
       divElement.classList.toggle("light-theme");
       divElement.classList.toggle("dark-theme");
       sessionStorage.setItem('forTheme', divElement.classList);
       var divElement = document.querySelector("#divTheme");
       divElement.classList.toggle("light-theme");
       divElement.classList.toggle("dark-theme");
       sessionStorage.setItem('divTheme', divElement.classList);
    });

    $("#swapColorsMobilexs").click( function(event) {
        sessionStorage.clear();
       var divElement = document.querySelector("#forTheme");
       divElement.classList.toggle("light-theme");
       divElement.classList.toggle("dark-theme");
       sessionStorage.setItem('forTheme', divElement.classList);
       var divElement = document.querySelector("#divTheme");
       divElement.classList.toggle("light-theme");
       divElement.classList.toggle("dark-theme");
       sessionStorage.setItem('divTheme', divElement.classList);
    });
});