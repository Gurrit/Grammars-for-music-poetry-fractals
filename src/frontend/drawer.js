function CreateDrawer(canvas) {
  let self = this;
  self.drawings = [];
  self.penStyle = "black";
  self.penWidth = 1;
  self.context = canvas.getContext("2d");
  self.height = canvas.height;
  self.width = canvas.width;

  self.draw = function(coordinate1, coordinate2) {
    self.context.moveTo(coordinate1.x, coordinate1.y);
    self.context.lineTo(coordinate2.x, coordinate2.y);
    self.drawings.push(new line(coordinate1, coordinate2));
    self.context.stroke();
  };
  self.extract = function(inputString) {
    let [x, y] = inputString.split(", ");
    let xInt = Number(x) + self.width / 2;
    let yInt = Number(y) + self.height / 2;
    return new coordinate(xInt, yInt);
  };
  self.scale = function(factor) {
    self.context.scale(factor, factor);
    self.redraw();
  };
  self.reset = function() {
    const context = canvas.getContext("2d");
    console.log("reseting ");
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = "rgba(255, 255, 255, 1)";
    context.beginPath();
  };
  self.redraw = function() {
    for (let drawing in self.drawings) {
      let c1 = drawing.c1;
      let c2 = drawing.c2;
    }
  };

  self.color = function(hexkod) {
    let ctx = canvas.getContext("2d");
    ctx.strokeStyle = hexkod;

    //self.context = context;
  };
  return self;
}

class coordinate {
  constructor(x, y) {
    let self = this;
    self.x = x;
    self.y = y;
    return self;
  }
}
class line {
  constructor(c1, c2) {
    let self = this;
    self.c1 = c1;
    self.c2 = c2;
  }
}
