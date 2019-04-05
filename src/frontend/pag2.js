function listenToFractal() {
  var audio = new Audio("audio_file.mp3");
  audio.play();
}

function toPianoJson(data, type, mode, iter, step) {
  var string =
    "{" +
    '"data":' +
    '"' +
    data +
    '", ' +
    '"type":' +
    '"' +
    type +
    '", ' +
    '"mode":' +
    '"' +
    mode +
    '", ' +
    '"iteration":' +
    iter +
    ", " +
    '"step":' +
    step +
    "}";
  return string;
}

function sendNotes() {
  var notes = JSON.stringify(noteArray);
  var pianoJson = toPianoJson(noteArray, "Sierpinski", "piano", "3", "20"); //TODO: select fractal
  console.log(notes);
  sendMessage(pianoJson);
  noteArray = [];
}

function main() {
  addFractalOptions("selectFractal3");

  connectToServer();
}
