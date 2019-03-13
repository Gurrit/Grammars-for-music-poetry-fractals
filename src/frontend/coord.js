function getCursorPosition(canvas, event) {
  var rect = canvas.getBoundingClientRect();
  var x = event.clientX - rect.left;
  var y = event.clientY - rect.top;
  console.log("x: " + x + " y: " + y);
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
  drawCanvas = document.getElementById("canvas1");

  let turtle = new CreateTurtle(drawCanvas);

  console.log("Before X,Y" + turtle.position().toString());
  turtle.forward(50);
  console.log("After X,Y" + turtle.position().toString());
  canvas = turtle.canvas();

  console.log(canvas.width.toString());
}
