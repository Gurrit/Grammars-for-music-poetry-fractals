function getCursorPosition(canvas, event) {
  var rect = canvas.getBoundingClientRect();
  var x = event.clientX - rect.left;
  var y = event.clientY - rect.top;
  console.log("x: " + x + " y: " + y);
}

function drawTurtle() {
  var turtle;
  var count = 0;
  if (count == 0) {
    let turtle = new CreateTurtle(document.getElementById("canvas1"));
    count = count + 1;
  }
  console.log(turtle.position().toString());
  turtle.forward(50);
  console.log(turtle.position().toString());
  count = count - 1;
}
