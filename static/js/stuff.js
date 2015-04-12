
var frm = $("#downloadForm");
frm.submit(function (ev) {
    $.ajax({
        type:"post",
        url: "/downloadsubmit/",
        data: frm.serialize(),
        success: function (data) {
            var content=$(data);
            $("#result").val(content)
        }
    });
    console.log(frm.serialize());

    ev.preventDefault();
    return false;
});

// Attach a submit handler to the form
var frm2 = $("#uploadForm");
frm2.submit(function (ev) {
    $.ajax({
        type:"post",
        url: "/uploadsubmit/",
        data: new FormData(this),
        processData: false,
        contentType: false,
        success: function (data) {
            $("#resulta").val(content)
            
        }
    });
    console.log(frm2.serialize());
    ev.preventDefault();
    return false;
});