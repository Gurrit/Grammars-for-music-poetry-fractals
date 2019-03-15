var fractalList = new Array();

function getCursorPosition(canvas, event) {
  var rect = canvas.getBoundingClientRect();
  var x = event.clientX - rect.left;
  var y = event.clientY - rect.top;
  var str = "x:" + x + "," + "y:" + y;

  console.log("'{" + str + "}'");
  return "'{" + str + "}'";
}

function optionValue(text, jsonFractal, maxIter) {
  this.text = text;
  this.jsonFractal = jsonFractal;
  this.maxIter = maxIter;
}

function addFractalOptions(selectID) {
  //type = text (det som syns), maxIter = maximum of iterations, jsonFractal (det som skickas till server)
  var select = document.getElementById(selectID);
  for (index in fractalList) {
    select.options[select.options.length] = new Option(fractalList[index].text);
    console.log(fractalList[index].text);
  }
}

function addIterOptions(valueFractal, selectID) {
  max = 0;
  var select = document.getElementById(selectID);

  for (index in fractalList) {
    console.log(fractalList[index].jsonFractal);
    if (fractalList[index].jsonFractal == valueFractal) {
      max = fractalList[index].maxIter;
      for (i = 1; i < max + 1; i++) {
        select.options[select.options.length] = new Option(i);
        console.log(fractalList[index].text);
      }
      break;
    }
  }
  maxIter = fractalList[index].text;
}

function main() {
  var sierpinski = new optionValue("Sierpinski Triangle", "Sierpinski", 10);
  fractalList.push(sierpinski);
  var dragon = new optionValue("Dragon Curve", "Dragon", 10);
  fractalList.push(dragon);
  var gosper = new optionValue("Gosper Curve", "Gosper", 3);
  fractalList.push(gosper);
  var koch = new optionValue("Square Koch Snowflake", "Koch", 7);
  fractalList.push(koch);

  addFractalOptions("selectFractal1");
  addFractalOptions("selectFractal2");
  addIterOptions("Sierpinski", "selectIter1");

  console.log(fractalList);
}

function sendCursorPosition(canvas, event) {
  getCursorPosition(canvas, event);

  //TODO send coordinates to server
}

function setCanvasSize(canvas, size) {
  //verkar inte funka, varför????
  drawCanvas = document.getElementById(canvas);
  console.log(drawCanvas);
  drawCanvas.width = size;
  drawCanvas.height = size;
}

//{"type":"Sierpinski",

//"iteration":3,

//"step":3 }

function getOption(dropdown) {
  var e = document.getElementById(dropdown);
  var selected = e.options[e.selectedIndex].value;

  return selected;
}

function drawTurtle() {
  var option1 = getOption("selectFractal1");
  var option2 = getOption("selectFractal2");
  console.log(option1.toString());

  jsonStr =
    "f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f l:90 f r:90 f l:90 f l:90 f r:90 f r:90 f r:90 f l:90 f l:90 f r:90 f";

  msg = '{"type":"Sierpinski", "iteration":5, "step":5}';

  switch (option1) {
    case "None":
      break;
    case "Sierpinski Triangle":
      console.log(msg);
      sendMessage(msg);
      break;
    case "Square Koch Snowflake":
      break;
    case "Gosper Curve":
      break;
    case "Dragon Curve":
      break;
  }

  console.log("kommer vi hit?" + option1.toString());
  drawCanvas = document.getElementById("canvas1");
  let turtle = new CreateTurtle(drawCanvas);
  //TODO Send to server for utskrivning
  //console.log("Before X,Y" + turtle.position().toString());

  for (var i = 0; i < jsonStr.length; i++) {
    if (jsonStr.charAt(i) == " ") {
      i++;
    }
    if (jsonStr.charAt(i) == "f") {
      //savePos(start, end);
      turtle.forward(5);
    }
    if (jsonStr.charAt(i) == "r") {
      degree1 = "";
      degree1 += jsonStr.charAt(i + 2);
      degree1 += jsonStr.charAt(i + 3);

      turtle.right(degree1);
    }
    if (jsonStr.charAt(i) == "l") {
      degree2 = "";
      degree2 += jsonStr.charAt(i + 2);
      degree2 += jsonStr.charAt(i + 3);

      turtle.left(degree2);
    }

    //turtle.forward(50);
    //console.log("After X,Y" + turtle.position().toString());
    canvas = turtle.canvas();

    //console.log(canvas.width.toString());
  }

  if (option2 != "None") {
    //TODO Translate from option1 to option2 via server and draw the desired fractal here
  }
}
