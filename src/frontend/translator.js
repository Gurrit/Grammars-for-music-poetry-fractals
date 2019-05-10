function drawNewFractal(lines, drawer, fractal, iteration) {

    drawer.reset();
    let len = lines.length;
    for (let line = 0; line < len; line++) {
        let coordinate1 = new Coordinate(lines[line].coordinate1.x, lines[line].coordinate1.y);
        let coordinate2 = new Coordinate(lines[line].coordinate2.x, lines[line].coordinate2.y);
        let color = lines[line].color;
        drawer.saveNewLine(coordinate1, coordinate2, color);
    }
    drawer.scaleToSize();
    drawer.saveFractal(fractal, iteration);
}

function translateFractal(lines, drawer, newColor) {
    let savedLines = drawer.drawings.slice();
    let len = lines.length;
    drawer.reset();
    console.log(savedLines);
    for (let line = 0; line < len; line++) {
        let coordinate1 = new Coordinate(lines[line].coordinate1.x, lines[line].coordinate1.y);
        let coordinate2 = new Coordinate(lines[line].coordinate2.x, lines[line].coordinate2.y);
        drawer.saveNewTranslatedLine(coordinate1, coordinate2, newColor);
    }
    drawer.drawings = drawer.drawings.concat(savedLines);
    console.log(drawer.drawings);
    drawer.scaleToSize();
}