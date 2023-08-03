$(document).ready(function() {
    var url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
    $.ajax({
        url: url,
        datatype: "json",
        success: function(data) {
            var name = data.name;
            $("#character").text(name);
        }
    });
});
