function listenToFractal() {
  var audio = new Audio("audio_file.mp3");
  audio.play();
}

function show_image(src, width, height, alt) {
  var img = document.createElement("img");
  img.src = src;
  img.width = width;
  img.height = height;
  img.alt = alt;

  // This next line will just add it to the <body> tag
  document.body.appendChild(img);
}
function main() {}
