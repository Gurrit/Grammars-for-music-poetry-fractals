let isPianoMode = false;

function sendNotes() {
  let optionIter1 = getOption("selectIter1");
  let optionFracs = [getOption("selectFractal1"), getOption("selectFractal2")];
  let canvases = [
    document.getElementById("canvas1"),
    document.getElementById("canvas2")
  ];
  let type = "draw";
  isPianoMode = false;
  let value = "";
  for (canvas in canvases) {
    for (index in fractalList) {
      if (fractalList[index].text === optionFracs[canvas].value) {
        value = fractalList[index].jsonFractal;
        break;
      }
    }

    if (noteArray.length !== 0) {
      type = "piano";
      isPianoMode = true;
    }
    let msg = toJson(canvas, noteArray, value, type, optionIter1.value);
    sendMessage(msg);
  }
  noteArray = [];
}

function resetPiano() {
  noteArray = [];
  document.getElementById("notesText").innerHTML = "";
}

function startPianoUI() {
  createFractalList();
  let turtcanv1 = new TurtleCanvasObj("canvas1");
  let turtcanv2 = new TurtleCanvasObj("canvas2");
  canvasTurtleList.push(turtcanv1);
  canvasTurtleList.push(turtcanv2);
  connectToServer([turtcanv1, turtcanv2]);
  addFractalOptions("selectFractal1");
  addFractalOptions("selectFractal2");
  hideElement("loadingbar", "display");
  changetext(false);
}

function sendCursorPosition(canvas, event) {
  //should probably not be hardcoded
  let translationIteration = getOption("selectTranslationIteration");
  let drawer = canvasTurtleList[0].turtlen;
  let fromFractal = canvasTurtleList[0].turtlen.fractal;
  let toFractal = canvasTurtleList[1].turtlen.fractal;
  if (fromFractal === null || toFractal === null) {
    alert("something has gone wrong, not sending the message");
    return;
  }
  let coordinate = getCursorPosition(canvas, event, drawer.transformation);
  let message = coordinateToJson(
    coordinate,
    fromFractal.fractal,
    fromFractal.iteration,
    toFractal.fractal,
    translationIteration.value,
    fromFractal.modified
  );

  if (!isPianoMode) {
    sendMessage(message);
  }
}

function getCursorPosition(canvas, event, transformation) {
  //get the position of the cursor on the canvas
  let rect = canvas.getBoundingClientRect();
  let x =
    (event.clientX - rect.left - rect.width / 2) / transformation.scale -
    transformation.position.x;
  let y =
    (event.clientY - rect.top - rect.height / 2) / transformation.scale -
    transformation.position.y;

  return new Coordinate(x, y);
}
