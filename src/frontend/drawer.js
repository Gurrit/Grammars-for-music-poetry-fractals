function CreateDrawer(canvas) {
    let self = this;
    self.penStyle = 'black';
    self.penWidth = 1;
    self.context = canvas.getContext('2d');
    self.height = canvas.height;
    self.width = canvas.width;
    self.draw = function (coordinate1, coordinate2) {
        self.context.moveTo(coordinate1.x, coordinate1.y);
        self.context.lineTo(coordinate2.x, coordinate2.y);
        self.context.stroke();
    };
    self.extract = function(inputString) {
        let [x, y] = inputString.split(", ");
        let xInt = Number(x) + (self.width / 2);
        let yInt = Number(y) + (self.height / 2);
        return new coordinate(xInt, yInt);
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