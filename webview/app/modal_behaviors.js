$('#createModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var template = button.data('template') // Extract info from data-* attributes
    var template_verbose = button.html() // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this)

    modal.find('.modal-title').text('Create a ' + template_verbose)
    modal.find('#input_template').val(template);

    if(template == 'matrix') {
        modal.find('#key-field').show();
        modal.find('#key-field-2').show();
    } else {
        modal.find('#key-field').hide();
        modal.find('#key-field-2').hide();
    }
});