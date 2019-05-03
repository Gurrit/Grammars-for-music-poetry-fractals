function finishedLoadingBtn() {
  changetext(false);
  hideelement("loadingbar", "display");
}

function startedLoadingBtn() {
  changetext(true);
  showelement("loadingbar", "display");
}

function finishedmusic() {
  showelement("canv2play", "display");
}

function hidemusic(id) {
  hideelement(id, "display");
  showelement("musicloading2", "display");
}

function hideelement(id, format) {
  //visbility for text, and display for divs and such
  var x = document.getElementById(id);

  if (format == "display") {
    x.style.display = "none";
  } else if (format == "visibility") {
    x.style.visbility = "hidden";
  }
}

function changetext(loading) {
  var btntext = document.getElementById("buttontext");

  if (loading) {
    btntext.innerText = "Loading";
  } else if (!loading) {
    btntext.innerText = "Generate Fractals";
  }
}

function showelement(id, format) {
  //visbility for text, and display for divs and such
  var x = document.getElementById(id);

  if (format == "display") {
    x.style.display = "inline-block";
  } else if (format == "visibility") {
    x.style.visbility = "initial";
  }
}

function sendNotes() {
  let optionIter1 = getOption("selectIter1");
  let optionFracs = [getOption("selectFractal1"), getOption("selectFractal2")];
  let canvases = [
    document.getElementById("canvas1"),
    document.getElementById("canvas2")
  ];
  type = "draw";
  var value = "";
  for (canvas in canvases) {
    for (index in fractalList) {
      if (fractalList[index].text === optionFracs[canvas].value) {
        value = fractalList[index].jsonFractal;
        break;
      }
    }

    if (noteArray.length !== 0) {
      type = "piano";
    }
    msg = toJson(canvas, noteArray, value, type, optionIter1.value);
    sendMessage(msg);
    console.log(msg);
  }
  noteArray = [];
}

function resetPiano() {
  noteArray = [];
  document.getElementById("notesText").innerHTML = "";
}

function startPianoUI() {
  createFractalList();
  let turtcanv1 = new TurtleCanvasobj("canvas1");
  let turtcanv2 = new TurtleCanvasobj("canvas2");
  canvasturtlelist.push(turtcanv1);
  canvasturtlelist.push(turtcanv2);
  connectToServer([turtcanv1, turtcanv2]);
  addFractalOptions("selectFractal1");
  addFractalOptions("selectFractal2");
  hideelement("loadingbar", "display");
  changetext(false);
}

function sendCursorPosition(canvas, event) {
  //should probably not be hardcoded
  let drawer = canvasturtlelist[0].turtlen;
  let fromFractal = canvasturtlelist[0].turtlen.fractal;
  let toFractal = canvasturtlelist[1].turtlen.fractal;
  if (fromFractal === null || toFractal === null) {
    alert("something has gone wrong, not sending the message");
    return;
  }
  let coordinate = getCursorPosition(canvas, event, drawer.transformation);
  let message = coordinateToJson(
    coordinate,
    fromFractal.fractal,
    fromFractal.iteration,
    toFractal.fractal
  );
  console.log("koordinatmeddelandet" + message);
  sendMessage(message);
}

function getCursorPosition(canvas, event, transformation) {
  //get the position of the cursor on the canvas
  var rect = canvas.getBoundingClientRect();
  var x =
    (event.clientX - rect.left - rect.width / 2) / transformation.scale -
    transformation.position.x;
  var y =
    (event.clientY - rect.top - rect.height / 2) / transformation.scale -
    transformation.position.y;
  console.log(x);
  console.log(y);
  var str = "x:" + x + "," + "y:" + y;

  console.log("'{" + str + "}'");
  return "'{" + str + "}'";
}
