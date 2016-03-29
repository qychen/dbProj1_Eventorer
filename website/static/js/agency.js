/*!
 * Start Bootstrap - Agency Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Highlight the top nav as scrolling occurs
$('body').scrollspy({
    target: '.navbar-fixed-top'
})

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});

var baseURL = "/"
/*
var names = document.getElementsByClassName("names");

var detailClick = function() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
        	//alert(xmlHttp.responseText);
        	var res = JSON.parse(xmlHttp.responseText);
        }
    }
    url = baseURL + "event" + "/roy";
    xmlHttp.open("GET", url, true); // true for asynchronous 
    xmlHttp.send(null);
};

for (var i = 0; i < names.length; i++) {
    names[i].addEventListener('click', detailClick, false);
}
*/

$('#search').keyup(function (e) {
    if (e.keyCode === 13) {
        if (!this.value)
            alert("Please enter some keywords for search!");
        else{
            /*
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = function() { 
                if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
                    //alert(xmlHttp.responseText);
                    var res = JSON.parse(xmlHttp.responseText);
                }
            }
            url = baseURL + "search?keywords=" + this.value;
            xmlHttp.open("GET", url, true); // true for asynchronous 
            xmlHttp.send(null);
            */
            window.location = "search?keywords=" + this.value;

        }




    }
});










