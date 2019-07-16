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


$.ajax({
    url: "http://localhost:8000/api/notes/",
    context: document.body
}).done(function(response) {
    response.forEach(function(element) {
        console.log(element);
        $("#recentfiles").append(`
        <div class = 'col-md-3'>
            <div class="card" style="width: 13rem; height: 14rem;">
                <a href="${element.google_doc_url}" target='_blank'>
                <div class="card-body">
                    <img src="images/word.png" class="card-img-top" alt="...">
                    <p class="card-text text-center">${element.title}</p>
                </div>
                </a>
            </div>
        </div>
        `);
    });
    
});
