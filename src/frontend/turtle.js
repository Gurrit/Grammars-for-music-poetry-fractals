function CreateTurtle(canvas) {
    let self = this;
    let rotation = 90;
    let position = {
        x: canvas.width / 2 + 0.5,
        y: canvas.height / 2 + 0.5
    };
    let isPenDown = true;
    let toRadians = function (r) {
        return 2 * Math.PI * (r / 360)
    };
    let rotate = function (deg) {
        rotation = (rotation + deg) % 360;
        if (rotation < 0) rotation += 360;
    };
    self.penStyle = 'black';
    self.penWidth = 1;
    self.penUp = function() { isPenDown = false;
    };
    self.penDown = function() {
        isPenDown = true;
    };
    self.forward = function(pixels) {
        let origX = position.x, origY = position.y;
        position.x += Math.cos(toRadians(rotation)) * pixels;
        position.y -= Math.sin(toRadians(rotation)) * pixels;
        if (!isPenDown) {
            return;
        }
        let context = canvas.getContext('2d');
        context.strokeStyle = self.penStyle;
        context.lineWidth = self.penWidth;
        context.beginPath();
        context.moveTo(origX, origY);
        context.lineTo(position.x, position.y);
        context.stroke();
    };
    self.left = function(deg) {
        rotate(deg);
    };
    self.right = function(deg) {
        rotate(-deg);
    };
    self.goto = function (position) {

    };
    return self;
}