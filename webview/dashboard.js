var templates = ['blank', 'matrix', 'cornell']
var clickable = true;
// TextBox slide down and up
$('.textBox').each(function (i) {
    $('.' + templates[i]).on('click', function () {
        if (clickable === true) {
            $('.textBox').css('display', 'none');
            $('.' + templates[i] + 'Form').slideDown();
            clickable = false;
        }
    })
    $('#' + templates[i] + 'Delete').on('click', function () {
        $('.' + templates[i] + 'Form').slideUp();
        clickable = true;
    })
})