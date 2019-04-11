globalStep = 25;

function start() {
  createFractalList();
  //skapar elementen till listorna och turtlecanvasobjekten
  let turtcanv1 = new TurtleCanvasobj("canvas1");
  let turtcanv2 = new TurtleCanvasobj("canvas2");
  canvasturtlelist.push(turtcanv1);
  canvasturtlelist.push(turtcanv2);
  addFractalOptions("selectFractal1");
  addFractalOptions("selectFractal2");


  connectToServer([turtcanv1, turtcanv2]);
}

function getStartPos(canvas, startpos) {
  //getting startposition for corresponding fractal
  switch (startpos) {
    case "bottomleftcorner":
      x = 0;
      y = canvas.height;
      break;
    case "middle":
      x = canvas.width / 2 + 0.5;
      y = canvas.height / 2 + 0.5;
      break;
  }

  console.log("x: " + x + "y: " + y);

  return [x, y];
}
function getCursorPosition(canvas, event, transformation) {
  //get the position of the cursor on the canvas
  var rect = canvas.getBoundingClientRect();
  var x = ((event.clientX - rect.left - (rect.width/2)) / transformation.scale) - transformation.position.x;
  var y = ((event.clientY - rect.top - (rect.height/2)) / transformation.scale) - transformation.position.y;
  console.log(x);
  console.log(y);
  var str = "x:" + x + "," + "y:" + y;

  console.log("'{" + str + "}'");
  return "'{" + str + "}'";
}

function coordinateToJson(coordinate, fractal, iteration) {
  return "{" +
      '"mode":"coordinate", ' +
      '"coordinate":"' + coordinate + '", ' +
      '"type":"' + fractal + '", ' +
      '"iteration":"' + iteration + '"' +
      "}";
}

function sendCursorPosition(canvas, event) {
  let len = canvasturtlelist.length;
  let drawer = null;
  let fractal = null;
  for (let i = 0; i < len; i++) {
    if (canvasturtlelist[i].canvasen === canvas) {
      drawer = canvasturtlelist[i].turtlen;
      fractal = drawer.fractal;
      break;
    }
  }
  console.log(canvasturtlelist);
  fractal = canvasturtlelist[1].turtlen.fractal;
  if(fractal === null) {
    alert("something has gone wrong, not sending the message");
    return;
  }
  let coordinate = getCursorPosition(canvas, event, drawer.transformation);
  let message = coordinateToJson(coordinate, fractal.fractal, fractal.iteration);
  sendMessage(message);
}
function toJson(turtleN, type, iter, step) {
  empty = [];
  var string =
    "{" +
    '"mode":' +
    '"draw", ' +
    '"data":' +
    '"' +
    empty +
    '", ' +
    '"index":' +
    '"' +
    turtleN +
    '", ' +
    '"type":' +
    '"' +
    type +
    '", ' +
    '"iteration":' +
    iter +
    ", " +
    '"step":' +
    step +
    "}";
  return string;
}

function sendDrawMessage() {
  //sends the actual message corresponding to what fractals and iterations are picked
  let optionIter1 = getOption("selectIter1");
  let optionFracs = [getOption("selectFractal1"), getOption("selectFractal2")];
  let canvases = [
    document.getElementById("canvas1"),
    document.getElementById("canvas2")
  ];
  var value = "";
  for (canvas in canvases) {
    for (index in fractalList) {
      if (fractalList[index].text === optionFracs[canvas].value) {
        value = fractalList[index].jsonFractal;
        //let turtle = getTurtle(canvases[canvas]);
        console.log("Startpos: " + fractalList[index].startpos);

        let array = getStartPos(canvases[canvas], fractalList[index].startpos);
        break;
      }
    }
    let msg = toJson(canvas, value, optionIter1.value, globalStep);
    console.log("meddelandet: " + msg);
    sendMessage(msg);
  }
}
