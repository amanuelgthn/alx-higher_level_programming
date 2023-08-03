$(document).ready(function() {
    $("#add_item").click(function() {
        var li = $("<li>Item</li>");
        $(".my_list").append(li);
    });
});
