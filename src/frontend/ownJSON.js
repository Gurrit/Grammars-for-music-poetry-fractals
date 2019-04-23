const globalStep = 25;

function toJson(canvasNumber, notes, fractal, mode, iterations) {
  //the number of the canvas (0 or 1), data = notes, type = fractal, mode = draw, piano or coordinate or play
  var string =
    "{" +
    '"index":' +
    '"' +
    canvasNumber +
    '",' +
    '"data":' +
    '"' +
    notes +
    '", ' +
    '"type":' +
    '"' +
    fractal +
    '", ' +
    '"mode":' +
    '"' +
    mode +
    '", ' +
    '"iteration":' +
    iterations +
    ", " +
    '"step":' +
    globalStep +
    "}";
  return string;
}

function coordinateToJson(coordinate, fromFractal, iteration, toFractal) {
  return (
    "{" +
    '"mode":"coordinate", ' +
    '"coordinate":"' +
    coordinate +
    '", ' +
    '"type":"' +
    fromFractal +
    '", ' +
    '"iteration":"' +
    iteration +
    '", ' +
    '"to":"' +
    toFractal +
    '"' +
    "}"
  );
}
