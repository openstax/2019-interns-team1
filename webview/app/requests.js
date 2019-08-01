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
            <div class="col-lg-6 d-flex">
                <div class="card mb-3">
                    <div class="row">
                        <div class="col-3">
                            <a href="${element.google_doc_url}" target="_blank" onclick="updateLastOpened(note='${element.id}');">
                                <docicon>
                                    <span class="fa-layers fa-fw">
                                        <i class="fas fa-${templates[element.template].icon}"></i>
                                        <span class="fa-layers-text fa-inverse" data-fa-transform="shrink-14 down-6" style="font-weight:900; background-color:#000;">${templates[element.template].short}</span>
                                    </span>
                                </docicon>
                            </a>
                        </div>
                        <div class="col-9">
                            <div class="card-body">
                                <a href="${element.google_doc_url}" target="_blank" onclick="updateLastOpened(note='${element.id}');">
                                    <h5 class="card-title mb-0">${element.title}</h5>
                                </a>
                                <p class="card-text small text-muted" id="star" data-note="" data-toggle="false">
                                    <span class="starring" onclick="toggleStar(note='${element.id}', star='${!element.star}');">${element.star ? `<i class="fas fa-star"></i> Important` : `<i class="far fa-star"></i>`}</span>
                                </p>
                                <p class="card-text">${element.tags ? `<span class="badge badge-${tags[element.tags].banner}">${tags[element.tags].verbose}</span>` : ''}</p>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer">
                        <small class="text-muted" id="timetoggler">
                            <span class="time-opened"><i class="far fa-clock"></i> <abbr title="info">Last opened ${moment(element.last_open_time).fromNow()}</abbr></span>
                            <span class="time-created"><i class="far fa-clock"></i> <abbr  title="info">Created ${moment(element.creation_time).fromNow()}</abbr></span>
                        </small>
                    </div>
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

function updateLastOpened(note=null) {
    if (note === null) {
        alert("Note cannot be null. Please sepcify a note ID to proceed.")
        return;
    }

    $.ajax({
        type: "PUT",
        url: cmsurl+"/api/notes/"+note+"/",
        data: {
            'do_update_lastopen': true
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