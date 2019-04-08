function CreateDrawer(canvas) {
    let self = this;
    self.drawings = [];
    self.penStyle = 'black';
    self.penWidth = 1;
    self.context = canvas.getContext('2d');
    self.height = canvas.height;
    self.width = canvas.width;
    self.context.transform(1, 0, 0, 1, self.width/2, self.height/2);
    self.draw = function (coordinate1, coordinate2) {
        self.context.moveTo(coordinate1.x, coordinate1.y);
        self.context.lineTo(coordinate2.x, coordinate2.y);
    };
    self.saveNewLine = function (coordinate1, coordinate2) {
        self.drawings.push(new Line(coordinate1, coordinate2));
    };
    self.extract = function(inputString) {
        let [x, y] = inputString.split(", ");
        let xInt = Number(x);
        let yInt = Number(y);
        return new Coordinate(xInt, yInt);
    };
    self.reset = function() {
        self.context.fillStyle = "rgba(255, 255, 255, 1)";
        self.context.clearRect(-canvas.width, -canvas.height, canvas.width*2, canvas.height*2);
        self.context.beginPath();
    };
    self.redraw = function () {
        for(let drawing in self.drawings) {
            let c1 = self.drawings[drawing].c1;
            let c2 = self.drawings[drawing].c2;
            self.draw(c1, c2);
        }
        self.context.stroke();
    };
    self.scaleToSize = function () {        // Make sure efficiency.
            let maxX = Math.max.apply(null, self.drawings.map(a=>a.c2.x > a.c1.x ? a.c2.x : a.c1.x));
            let maxY = Math.max.apply(null, self.drawings.map(a=>a.c2.y > a.c1.y ? a.c2.y : a.c1.y));
            let minX = Math.min.apply(null, self.drawings.map(a=>a.c2.x < a.c1.x ? a.c2.x : a.c1.x));
            let minY = Math.min.apply(null, self.drawings.map(a=>a.c2.y < a.c1.y ? a.c2.y : a.c1.y));
            let centerX = (Math.abs(maxX)- Math.abs(minX)) / 2;
            let centerY = (Math.abs(maxY) - Math.abs(minY)) / 2;
            let scaleX = self.width / (maxX - minX);
            let scaleY = self.height / (maxY - minY);
            let scale = Math.min(scaleX, scaleY);
            self.context.transform(scale*0.9, 0, 0, scale*0.9, 0, 0);
            self.context.transform(1, 0, 0, 1, -centerX, -centerY);
            self.redraw();
            console.log("has drawn the image")
    };
    return self;
}
class Line {
    constructor(c1, c2) {
        let self = this;
        self.c1 = c1;
        self.c2 = c2;
    }
}

class Coordinate {
    constructor(x, y) {
        let self = this;
        self.x = x;
        self.y = y;
        return self;
    }
}