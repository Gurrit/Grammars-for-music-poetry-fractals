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
  let fractoption = getOption("selectFractal3");
  let iteroption = getOption("selectIter3");

  var value = "";
  for (index in fractalList) {
    if (fractalList[index].text === fractoption.value) {
      value = fractalList[index].jsonFractal;
      console.log("The fractal value: " + value);
      //let turtle = getTurtle(canvases[canvas]);
      break;
    }
  }

  pianoJson = toPianoJson(
    "canvas3",
    noteArray,
    value,
    "piano",
    iteroption.value,
    "20"
  );

  console.log(notes);
  console.log(pianoJson);
  sendMessage(pianoJson);
  noteArray = [];
}

function resetPiano() {}

function startPianoUI() {
  createFractalList();
  let turtcanv3 = new TurtleCanvasobj("canvas3");
  canvasturtlelist.push(turtcanv3);
  connectToServer([turtcanv3]);
  addFractalOptions("selectFractal3");
  sendNotes();
}
