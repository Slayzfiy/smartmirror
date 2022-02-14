// SLIDER FUNCTIONS
$("#quoteSlider").on("input change", function() {
    $("#maximumLengthValue").text($(this).val());
    sliceQuote($(this).val())
});

function sliceQuote(length){
    let quote = "Know that although in the eternal scheme of things you are small, you are also unique and irreplaceable, as are all your fellow humans everywhere in the world."
    let cutted = quote.slice(0, length)
    $("#sampleQuote").text(cutted + "...");
}
// END


// AUTHOR SELECTION FUNCTION
$(document).ready(function() {
    $('#example-getting-started').multiselect({
        includeSelectAllOption: true,
        enableFiltering: true,
        selectedClass: "select"
    });
});
// END