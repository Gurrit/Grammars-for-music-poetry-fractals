function setFileURL(eventdata) {
  //creates the URL for the sent wav file
  objectURL = URL.createObjectURL(eventdata);
  console.log("Objecturl:" + objectURL.toString());

  playsong(objectURL);
}
function sendfiles() {
  //send information av what fractal to generate and listen to
  data = [];

  fractalopt = getOption("selectFractal3");
  iteropt = getOption("selectIter3");

  value = findFractalInSelect(fractalopt);

  msg2 = toMusicJson("", data, value, "play", iteropt.value, 25);

  sendMessage(msg2);
}

function playsong(src) {
  //play the song
  console.log(src);
  var audio = new Audio(src);
  audio.play();
}
function toMusicJson(canvas, data, type, mode, iter, step) {
  var string =
    "{" +
    '"index":' +
    '"' +
    "0" +
    '",' +
    '"data":' +
    '"' +
    data +
    '", ' +
    '"type":' +
    '"' +
    type +
    '", ' +
    '"mode":' +
    '"' +
    mode +
    '", ' +
    '"iteration":' +
    iter +
    ", " +
    '"step":' +
    step +
    "}";
  return string;
}
