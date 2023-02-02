$.getJSON("https://api.ipify.org?format=json", function (data) {
    $.ajax({
        type: "POST",
        contentType: "application/json;charset=utf-8",
        url: "{{url_for('test')}}",
        traditional: "true",
        data: JSON.stringify({ data }),
        dataType: "json"
    });
})