function CreateDrawer(canvas) {
  let self = this;
  self.fractal = null;
  self.drawings = [];
  self.tempDrawings = [];
  self.penWidth = 1;
  self.context = canvas.getContext("2d");
  self.height = canvas.height;
  self.width = canvas.width;
  self.transformation = null;
  self.color = "#000000";
  self.context.transform(1, 0, 0, 1, self.width / 2, self.height / 2);
  self.draw = function(coordinate1, coordinate2, color) {
    if (color !== self.color) {
      // optimizes drawing with different colors.
      self.context.stroke();
      self.context.beginPath();
      self.context.strokeStyle = color;
      self.color = color;
    }
    self.context.moveTo(coordinate1.x, coordinate1.y);
    self.context.lineTo(coordinate2.x, coordinate2.y);
  };
  self.saveNewLine = function(coordinate1, coordinate2, color) {
    self.drawings.push(new Line(coordinate1, coordinate2, color));
  };

  self.reset = function() {
    self.drawings = [];
    self.tempDrawings = [];
    self.context.setTransform(1, 0, 0, 1, self.width / 2, self.height / 2);
    self.transformation = null;
    self.context.fillStyle = "rgb(0, 0, 0,1)";
    self.context.clearRect(
      -canvas.width,
      -canvas.height,
      canvas.width * 2,
      canvas.height * 2
    );
    self.context.beginPath();
  };

  self.redraw = function() {
    self.context.lineWidth = self.penWidth;
    let dr = self.drawings.slice().concat(self.tempDrawings);
    for (let drawing in dr) {
      let c1 = dr[drawing].c1;
      let c2 = dr[drawing].c2;
      let color = dr[drawing].color;
      self.draw(c1, c2, color);
    }
    self.context.stroke();
  };

  self.scaleToSize = function() {
    let maxX = Math.max.apply(
      null,
      self.drawings.map(a => (a.c2.x > a.c1.x ? a.c2.x : a.c1.x))
    );
    let maxY = Math.max.apply(
      null,
      self.drawings.map(a => (a.c2.y > a.c1.y ? a.c2.y : a.c1.y))
    );
    let minX = Math.min.apply(
      null,
      self.drawings.map(a => (a.c2.x < a.c1.x ? a.c2.x : a.c1.x))
    );
    let minY = Math.min.apply(
      null,
      self.drawings.map(a => (a.c2.y < a.c1.y ? a.c2.y : a.c1.y))
    );
    let centerX = (Math.abs(maxX) - Math.abs(minX)) / 2;
    let centerY = (Math.abs(maxY) - Math.abs(minY)) / 2;
    let scaleX = self.width / (maxX - minX);
    let scaleY = self.height / (maxY - minY);
    let scale = Math.min(scaleX, scaleY) * 0.9;
    self.context.transform(scale, 0, 0, scale, 0, 0);
    self.context.transform(1, 0, 0, 1, -centerX, -centerY);
    self.redraw();
    self.transformation = new Transformation(
      scale,
      new Coordinate(-centerX, -centerY)
    );
    finishedLoadingBtn();
  };

  self.saveFractal = function(name, iteration, modified) {
    self.fractal = new Fractal(name, iteration, modified);
  };

  self.saveNewTranslatedLine = function(coordinate1, coordinate2, color) {
    self.tempDrawings.push(new Line(coordinate1, coordinate2, color));
  };
  return self;
}
class Line {
  constructor(c1, c2, color) {
    let self = this;
    self.c1 = c1;
    self.c2 = c2;
    self.color = color;
  }
}

class Fractal {
  // This should maybe contain all drawings aswell.
  constructor(fractal, iteration, modified) {
    let self = this;
    self.fractal = fractal;
    self.iteration = iteration;
    self.modified = modified;
  }
}
class Transformation {
  constructor(scale, position) {
    let self = this;
    self.scale = scale;
    self.position = position;
  }
}
