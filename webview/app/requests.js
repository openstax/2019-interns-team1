$("#createForm").submit(function(e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var url = form.attr('action');
    
    var content = {
        rows: $('#keyterms').val().split('\n'),
        cols: $('#keyterms-2').val().split('\n'),
    }

    form.find('#input_content').val(JSON.stringify(content))

    $('#createModal').modal('hide');
    showOverlay();

    $.ajax({
        type: "POST",
        url: url,
        data: form.serialize(), // serializes the form's elements.
        headers: {
            "Authorization": "Basic " + auth
        },
        success: function(data) {
            loadNotes();
            hideOverlay();

            var redirectWindow = window.open(data.google_doc_url, '_blank');
            redirectWindow.location;
        },
        error: function(xhr, ajaxOptions, thrownError) {
            hideOverlay();
            alert(xhr.responseText);
        }
    });
});

function loadNotes(title="", filtertags="") {
    $.ajax({
        url: cmsurl+"/api/notes/?title="+title+"&tags="+filtertags,
        context: document.body
    }).done(function(response) {
        $("#recent-notes").html('');
        response.forEach(function(element) {
            $("#recent-notes").append(`
            <div class="col-3 d-flex">
                <div class="card mb-4">
                    <a href="${element.google_doc_url}" target="_blank">
                        <div class="card-body text-center mb-4 mt-4">
                            <docicon class="mb-2"><i class="fas fa-${templates[element.template].icon}"></i></docicon>
                            <h5 class="mb-0 text-size-light">${element.title}</h5>

                            ${element.tags ? `<span class="badge badge-${tags[element.tags].banner}">${tags[element.tags].verbose}</span>` : ''} 
                        </div>
                    </a>
                </div>
            </div>
            `);
        });
    });
}

function toggleStar(note=null, star=false) {
    if (note === null) {
        alert("Note cannot be null. Please sepcify a note ID to proceed.")
        return;
    }

    $.ajax({
        type: "PUT",
        url: cmsurl+"/api/notes/"+note+"/",
        data: {
            'star': star
        },
        headers: {
            "Authorization": "Basic " + auth
        },
        success: function(data) {
            loadNotes();
        },
        error: function(xhr, ajaxOptions, thrownError) {
            alert(xhr.responseText);
        }
    });
}

function loadlFilteredNotes() {
    var searchtitle = $('#filter_search').val();
    var searchtags = ''

    $('#filter_tags input').each(function() { 
        if($(this).is(":checked")){
            searchtags = searchtags + $(this).data("tag") +','
        }
    });

    loadNotes(title=searchtitle, filtertags=searchtags);
}