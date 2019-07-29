function showOverlay() {
    document.getElementById("tipoverlay").style.display = "block";

    var randomtip = tips[Math.floor(Math.random()*tips.length)];
    $('#tip-header').html(randomtip[0]);
    $('#tip-text').html(randomtip[1]);
}

function hideOverlay() {
    document.getElementById("tipoverlay").style.display = "none";
}