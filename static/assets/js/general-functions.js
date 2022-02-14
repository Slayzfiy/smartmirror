function notify(message,type){
    $.notify({
        message: message,
        icon: "tim-icons icon-bell-55"
    },{
        type: type,
        timer: 1000,
    });
}

$(".restoreSettings").click(function(event)
{
    $("#modalBOX").prepend("<!-- Modal -->\n" +
        "<div class=\"modal fade\" id=\"exampleModalCenter\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"exampleModalLabel\" aria-hidden=\"true\">\n" +
        "  <div class=\"modal-dialog\" role=\"document\">\n" +
        "    <div class=\"modal-content bg-dark\">\n" +
        "      <div class=\"modal-header\">\n" +
        "        <h2 class=\"modal-title text-light\" id=\"exampleModalLabel\">Restore default Settings</h2>\n" +
        "        <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\">\n" +
        "          <span aria-hidden=\"true\">&times;</span>\n" +
        "        </button>\n" +
        "      </div>\n" +
        "      <div class=\"modal-body text-light\">\n" +
        "        Are you sure to restore to default settings?\n" +
        "      </div>\n" +
        "      <div class=\"modal-footer\">\n" +
        "        <button type=\"button\" class=\"btn btn-secondary\" data-dismiss=\"modal\">No</button>\n" +
        "        <button type=\"button\" class=\"btn btn-primary\">Yes</button>\n" +
        "      </div>\n" +
        "    </div>\n" +
        "  </div>\n" +
        "</div>");

    $("#exampleModalCenter").modal("show");
    event.preventDefault();
});

// GENERAL FUNCTIONS
let $fontBox = $('#fontSelection')
let $fontPlaceholder = $('#fontPlaceholder');
$fontBox.change(function (e){
    let $currentFont = $fontBox.val();
    $fontPlaceholder.css('font-family', $currentFont);
})
$("#slider").on("input change", function() {
    $("#font_size").text($(this).val());
    $("#sampleText").css("font-size", $(this).val() + "px");
});

// Default values from configuration are injected
function load_default_conf(configFontFamily, configFontSize, configBackgroundColor, configVisibility, grid_place){
    $("#font_size").text(configFontSize);
    $("#slider").val(configFontSize);

    // grausiger code
    let grid_place_id = "#grid-" + grid_place + "-input"
    $(grid_place_id).prop("checked", "true")


    let options = $('#fontSelection option');
    $('#fontPlaceholder').css('font-family', configFontFamily)
    var values = $.map(options,function(option) {
        if (configFontFamily === option.value){
            option.selected = true
        }
    });

    let visibilityCB = $('#visibility');
    let visibilityText = $('#visibilityText');

    if(configVisibility === "on"){
        visibilityCB.prop('checked', true)
    }
    else{
        visibilityCB.prop('checked', false)
    }

    checkVisibility()

    visibilityCB.change(function (){
        checkVisibility();
    })

    function checkVisibility(){
        if (visibilityCB.prop('checked') === true){
            visibilityText.text('shown');
            visibilityText.addClass('text-success');
            visibilityText.removeClass('text-danger');
        }
        else{
            visibilityText.text('now shown');
            visibilityText.addClass('text-danger');
            visibilityText.removeClass('text-success');
        }
    }
}

// Ajax function if form is submitted
$('form').submit(function (e) {
    $.ajax({
        type: "POST",
        url: "/config",
        data: $(this).serialize(),
        success:function (){
            notify('Successfully changed settings!', 'success')
        }
    })
    e.preventDefault();
});

// $('#export_config').click(function (e) {
//     $.ajax({
//         type: "GET",
//         url: "/export",
//         data: $(this).serialize(),
//         success:function (){
//             notify('Successfully changed settings!', 'success')
//         }
//     })
//     e.preventDefault();
// });

// GRID System, if one checkbox is selected and you click another, the first will be unchecked
$('.check').click(function() {
    $('.check').not(this).prop('checked', false);
});
