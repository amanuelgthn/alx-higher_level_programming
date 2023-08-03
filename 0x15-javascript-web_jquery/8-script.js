$(document).ready(function() {
    var url = "https://swapi-api.alx-tools.com/api/films/?format=json";
    $.ajax({
        url: url,
        datatype: "json",
        success: function(data) {
            var movies = data.results;
            var ul = $("UL#list_movies");
            for (var i = 0; i < movies.length; i++) {
                var movie = movies[i];
                var li = $("<li>" + movie.title + "</li>");
                ul.append(li);
             }
        }
    });
});
