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

function showpic() {
  var x = document.getElementById("help_picture");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
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
    "8"
  );

  console.log(notes);
  console.log(pianoJson);
  sendMessage(pianoJson);
  noteArray = [];
}

function resetPiano() {
  noteArray = [];
  document.getElementById("notesText").innerHTML = "";
}

function startPianoUI() {
  createFractalList();
  let turtcanv3 = new TurtleCanvasobj("canvas3");
  canvasturtlelist.push(turtcanv3);
  connectToServer([turtcanv3]);
  addFractalOptions("selectFractal3");
  sendNotes();
}
