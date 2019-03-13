function getCursorPosition(canvas, event) {
  var rect = canvas.getBoundingClientRect();
  var x = event.clientX - rect.left;
  var y = event.clientY - rect.top;
  console.log("x: " + x + " y: " + y);
}

function getOption(dropdown) {
  var e = document.getElementById(dropdown);
  var selected = e.options[e.selectedIndex].text;

  return selected;
}

function setCanvasSize() {
  drawCanvas1 = document.getElementById("canvas1");
  drawCanvas1.width = 500;
  drawCanvas1.height = 500;

  drawCanvas2 = document.getElementById("canvas2");
  drawCanvas2.width = 500;
  drawCanvas2.height = 500;
}

function drawTurtle() {
  var option1 = getOption("select1");
  var option2 = getOption("select2");

  if (option1 != "None") {
    console.log("kommer vi hit?" + option1.toString());
    drawCanvas = document.getElementById("canvas1");
    fractal = option1;
    let turtle = new CreateTurtle(drawCanvas);

    console.log("Before X,Y" + turtle.position().toString());
    turtle.forward(50);
    console.log("After X,Y" + turtle.position().toString());
    canvas = turtle.canvas();

    console.log(canvas.width.toString());
  }

  if (option2 != "None") {
    //Translate from option1 to option2 via server and draw the desired fractal here
  }
}
