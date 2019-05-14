const globalStep = 25;

function toJson(canvasNumber, notes, fractal, mode, iterations) {
  //the number of the canvas (0 or 1), data = notes, type = fractal, mode = draw, piano or coordinate or play
  return "{" +
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
}

function coordinateToJson(coordinate, fromFractal, iteration, toFractal, translationIteration, modified) {
  return (
    "{" +
    '"mode":"coordinate", ' +
    '"coordinate":{' +
    '"x":' +
    coordinate.x +
    ', ' +
    '"y":' +
    coordinate.y +
    '}, ' +
    '"type":"' +
    fromFractal +
    '", ' +
    '"iteration":"' +
    iteration +
    '", ' +
    '"translation_iteration":' +
    translationIteration +
    ', ' +
    '"modified":' +
    modified +
    ', '    +
    '"to":"' +
    toFractal +
    '"' +
    "}"
  );
}
