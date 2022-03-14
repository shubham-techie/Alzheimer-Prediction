var loadFile = function (event) {
    var image = document.getElementById('preview');
    image.src = URL.createObjectURL(event.target.files[0]);
}

