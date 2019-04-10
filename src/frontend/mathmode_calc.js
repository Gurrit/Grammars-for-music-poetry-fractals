const fractalList = [];
canvasturtlelist = [];
globalStep = 25;

function main() {
  //skapar elementen till listorna och turtlecanvasobjekten
  var sierpinski = new optionValue(
    "Sierpinski Triangle",
    "Sierpinski",
    10,
    "middle"
  );
  fractalList.push(sierpinski);
  var dragon = new optionValue("Dragon Curve", "Dragon", 10, "middle");
  fractalList.push(dragon);
  var gosper = new optionValue("Gosper Curve", "Gosper", 3, "middle");
  fractalList.push(gosper);
  var koch = new optionValue(
    "Square Koch Snowflake",
    "Koch",
    7,
    "bottomleftcorner"
  );
  fractalList.push(koch);
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
function getCursorPosition(canvas, event) {
  //get the position of the cursor on the canvas
  var rect = canvas.getBoundingClientRect();
  var x = event.clientX - rect.left;
  var y = event.clientY - rect.top;
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
  let coordinate = getCursorPosition(canvas, event);
  let len = canvasturtlelist.length;
  let fractal = null;
  for (let i = 0; i < len; i++) {
    if (canvasturtlelist[i].canvasen === canvas) {
      fractal = canvasturtlelist[i].turtlen.fractal;
    }
  }
  let message = coordinateToJson(coordinate, fractal.fractal, fractal.iteration);
  sendMessage(message);
}

function optionValue(text, jsonFractal, maxIter, startpos) {
  //create optionvalue objects for dropwodn menu
  //type = text (det som syns), maxIter = maximum of iterations, jsonFractal (det som skickas till server), startpos = middle or bottomleftcorner
  this.text = text;
  this.jsonFractal = jsonFractal;
  this.maxIter = maxIter;
  this.startpos = startpos;
}

function addFractalOptions(selectID) {
  //add the objects to the <select>
  //add the fractals to the select dropdown
  var select = document.getElementById(selectID);
  for (index in fractalList) {
    select.options[select.options.length] = new Option(fractalList[index].text);
  }
}

function selected() {
  //om man valt en viss fraktal ska vissa iterationer visas i dropdownmenyn
  var option1 = getOption("selectFractal1");
  var option2 = getOption("selectFractal2");
  addIterOptions(option1.value, "selectIter1");
}

function addIterOptions(textFractal, selectID) {
  //adding the iteration options corresponding to the fractal
  max = 0;
  var select = document.getElementById(selectID);
  //console.log(select.options);
  select.options.length = 0;

  for (index in fractalList) {
    if (fractalList[index].text == textFractal) {
      max = fractalList[index].maxIter;
      for (i = 1; i < max + 1; i++) {
        select.options[select.options.length] = new Option(i);
        //console.log(fractalList[index].text);
      }
      break;
    }
  }
  maxIter = fractalList[index].text;
}

function TurtleCanvasobj(canvas) {
  //creating objects sconsisting of a new turtle and the corresponding canvas
  let canvasen = document.getElementById(canvas);
  let drawer = new CreateDrawer(canvasen);
  let self = this;
  this.canvasen = canvasen;
  this.turtlen = drawer;
  return self;
}

function getTurtle(canvas) {
  //get the turtle corresponding to canvas
   console.log(canvasturtlelist);
  for (index in canvasturtlelist) {
    if (canvasturtlelist[index].canvasen === canvas) {
      return canvasturtlelist[index].turtlen;
    }
  }
}

function getOption(dropdown) {
  //get the option from one of the select
  var e = document.getElementById(dropdown);
  var selected = e.options[e.selectedIndex];
  //console.log(selected);

  return selected;
}

function toJson(turtleN, type, iter, step) {
  var string =
    "{" +
    '"mode":' +
    '"draw", ' +
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
        let turtle = getTurtle(canvases[canvas]);
        console.log("Startpos: " + fractalList[index].startpos);

        let array = getStartPos(canvases[canvas], fractalList[index].startpos);
        break;
      }
    }
    //resetCanvas("canvas1"); //måste rensa canvas och flytta turtle till början igen innan ny fraktal ritas
    let msg = toJson(canvas, value, optionIter1.value, globalStep);
    optionIter1.value
    console.log("meddelandet: " + msg);
    sendMessage(msg);
  }
}