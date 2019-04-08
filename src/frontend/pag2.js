function listenToFractal() {
  var audio = new Audio("audio_file.mp3");
  audio.play();
}

function toPianoJson(canvas, data, type, mode, iter, step) {
  var string =
    "{" +
    '"index":' +
    '"' +
    "0" +
    '",' +
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

  pianoJson = toPianoJson(
    "canvas3",
    noteArray,
    "Sierpinski",
    "piano",
    "3",
    "20"
  );
  console.log(notes);
  console.log(pianoJson);
  sendMessage(pianoJson);
  noteArray = [];
}

function startPianoUI() {
  createFractalList();
  let turtcanv3 = new TurtleCanvasobj("canvas3");
  canvasturtlelist.push(turtcanv3);
  connectToServer([turtcanv3]);
  addFractalOptions("selectFractal3");
  sendNotes();
}
