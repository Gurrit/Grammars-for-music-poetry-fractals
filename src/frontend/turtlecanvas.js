const canvasturtlelist = [];

class TurtleCanvasobj {
  constructor(canvas) {
    //creating objects sconsisting of a new turtle and the corresponding canvas
    let canvasen = document.getElementById(canvas);
    let drawer = new CreateDrawer(canvasen);
    let self = this;
    this.canvasen = canvasen;
    this.turtlen = drawer;
    return self;
  }
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
