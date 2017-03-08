$(window).load( function() {

    if (localStorage.getItem('forTheme')) {
        var theme1 = document.getElementById("forTheme");
        theme1.className = localStorage.getItem('forTheme');
    }
    if (localStorage.getItem('divTheme')) {
        var theme2 = document.getElementById("divTheme");
        theme2.className = localStorage.getItem('divTheme');
    }
    if (localStorage.getItem('font') && localStorage.getItem('fontname')) {
        var font = document.getElementById("swapFont");
        var fontname = document.getElementById("swapFontName");
        font.className = localStorage.getItem('font');
        fontname.innerHTML= localStorage.getItem('fontname');
    }
});

$(document).ready( function() {

    $("#swapColors").click( function(event) {
       localStorage.removeItem("forTheme");
       localStorage.removeItem("divTheme");
       var divElement = document.querySelector("#forTheme");
       divElement.classList.toggle("light-theme");
       divElement.classList.toggle("dark-theme");
       localStorage.setItem('forTheme', divElement.classList);
       var divElement = document.querySelector("#divTheme");
       divElement.classList.toggle("light-theme");
       divElement.classList.toggle("dark-theme");
       localStorage.setItem('divTheme', divElement.classList);
    });

    $("#swapColorsMobile").click( function(event) {
       localStorage.removeItem("forTheme");
       localStorage.removeItem("divTheme");
       var divElement = document.querySelector("#forTheme");
       divElement.classList.toggle("light-theme");
       divElement.classList.toggle("dark-theme");
       localStorage.setItem('forTheme', divElement.classList);
       var divElement = document.querySelector("#divTheme");
       divElement.classList.toggle("light-theme");
       divElement.classList.toggle("dark-theme");
       localStorage.setItem('divTheme', divElement.classList);
    });

    $("#swapColorsMobilexs").click( function(event) {
       localStorage.removeItem("forTheme");
       localStorage.removeItem("divTheme");
       var divElement = document.querySelector("#forTheme");
       divElement.classList.toggle("light-theme");
       divElement.classList.toggle("dark-theme");
       localStorage.setItem('forTheme', divElement.classList);
       var divElement = document.querySelector("#divTheme");
       divElement.classList.toggle("light-theme");
       divElement.classList.toggle("dark-theme");
       localStorage.setItem('divTheme', divElement.classList);
    });

    $("#swapFontName").click( function(event) {
        localStorage.removeItem("font");
        localStorage.removeItem("fontname");
        var divSwapFont = document.querySelector("#swapFont");
        divSwapFont.classList.toggle("serif-font");
        divSwapFont.classList.toggle("sans-font");
        localStorage.setItem('font', divSwapFont.classList);
        if (divSwapFont.className === "serif-font") {
            localStorage.setItem('fontname', "Change to Sans-serif");
            document.getElementById("swapFontName").innerHTML = "Change to Sans-serif"; 
        }
        else if (divSwapFont.className === "sans-font") {
            localStorage.setItem('fontname', "Change to Serif");
            document.getElementById("swapFontName").innerHTML = "Change to Serif";
        }
    });
});