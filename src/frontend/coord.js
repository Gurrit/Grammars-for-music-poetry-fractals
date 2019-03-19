var fractalList = new Array();
globalStep = 5;

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
    //console.log(fractalList[index].text);
  }
}

function selected() {
  var option1 = getOption("selectFractal1");
  var option2 = getOption("selectFractal2");
  console.log("HÄR??: " + option1.value.toString() + option2.value.toString());
  switch (option1.value) {
    case "None":
      break;
    case "Sierpinski Triangle":
      addIterOptions("Sierpinski", "selectIter1");
      break;
    case "Square Koch Snowflake":
      addIterOptions("Koch", "selectIter1");
      break;
    case "Gosper Curve":
      console.log("HÄR GOSPEr");
      addIterOptions("Gosper", "selectIter1");
      break;
    case "Dragon Curve":
      addIterOptions("Dragon", "selectIter1");
      break;
  }
}

function addIterOptions(valueFractal, selectID) {
  max = 0;
  var select = document.getElementById(selectID);
  //console.log(select.options);
  select.options.length = 0;

  for (index in fractalList) {
    if (fractalList[index].jsonFractal == valueFractal) {
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

function main() {
  var sierpinski = new optionValue("Sierpinski Triangle", "Sierpinski", 10);
  fractalList.push(sierpinski);
  var dragon = new optionValue("Dragon Curve", "Dragon", 10);
  fractalList.push(dragon);
  var gosper = new optionValue("Gosper Curve", "Gosper", 3);
  fractalList.push(gosper);
  var koch = new optionValue("Square Koch Snowflake", "Koch", 7);
  fractalList.push(koch);

  connectToServer();

  addFractalOptions("selectFractal1");
  addFractalOptions("selectFractal2");
}

function setCanvasSize(canvas, size) {
  //verkar inte funka, varför????
  drawCanvas = document.getElementById(canvas);
  drawCanvas.width = size;
  drawCanvas.height = size;
}

function getOption(dropdown) {
  var e = document.getElementById(dropdown);
  var selected = e.options[e.selectedIndex];
  //console.log(selected);

  return selected;
}

function toJson(type, iter, step) {
  var string =
    "{" +
    '"type":' +
    '"' +
    type +
    '",' +
    " " +
    '"iteration":' +
    iter +
    ", " +
    '"step":' +
    step +
    "}";
  return string;
}

function sendDrawMessage() {
  var optionFrac1 = getOption("selectFractal1");
  var optionIter1 = getOption("selectIter1");
  var optionFrac2 = getOption("selectFractal2");
  console.log(optionFrac1.toString());

  if (optionFrac2.value == "None") {
    console.log("härdå?");
    var value = "";
    for (index in fractalList) {
      if (fractalList[index].text == optionFrac1.value) {
        value = fractalList[index].jsonFractal;
        console.log("Text: " + fractalList[index].text);
        console.log("Value" + optionFrac1.value.toString());
        console.log("Högra optionet:" + value);
      }
    }

    //resetCanvas("canvas1");
    msg = toJson(value, optionIter1.value, globalStep);
    console.log("meddelandet: " + msg);
    sendMessage(msg);
  }
}

function resetCanvas(canvasValue) {
  const context = canvas.getContext(canvasValue);
  context.clearRect(0, 0, canvas.width, canvas.height);
}

function sendCursorPosition(canvas, event) {
  getCursorPosition(canvas, event);

  //TODO send coordinates to server
}
