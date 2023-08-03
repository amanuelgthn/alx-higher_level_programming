$(document).ready(function() {
    //select the header element and add class "red"
    $("DIV#toggle_header").click(function() {
        $("header").toggleClass("red").toggleClass("green");
    });
});