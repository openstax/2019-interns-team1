tags.forEach(function(element, key) {
    $('#filter_tags').append(`
    <div class="custom-control custom-switch">
        <input type="checkbox" class="custom-control-input" id="filter_tag_${key}" data-tag="${key}">
        <label class="custom-control-label" for="filter_tag_${key}">${element.verbose}</label>
    </div>
    `);
    $('#input_tags').append($("<option></option>")
        .attr("value",key)
        .text(element.verbose)); 
});

templates.forEach(function(element, key) {
    $('#filter_templates').append(`
    <li><i class="fas fa-${element.icon}"></i> ${element.verbose}</li>
    `);
});

$('#filter_search').change(function () {
    loadlFilteredNotes();
});

$('#filter_tags').on('change', 'input', function() {
    loadlFilteredNotes();
});