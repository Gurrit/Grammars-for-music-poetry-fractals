const canvasTurtleList = [];

class TurtleCanvasObj {
  constructor(canvasObject) {
    //creating objects consisting of a new turtle and the corresponding canvas
    let canvas = document.getElementById(canvasObject);
    let drawer = new CreateDrawer(canvas);
    let self = this;
    this.canvasen = canvas;
    this.turtlen = drawer;
    return self;
  }
}

function getTurtle(canvas) {
  //get the turtle corresponding to canvas
  for (let index in canvasTurtleList) {
    if (canvasTurtleList[index].canvasen === canvas) {
      return canvasTurtleList[index].turtlen;
    }
  }
}
