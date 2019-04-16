globalStep = 25;
fractalopt = "";
iteropt = "";
value = "";

function listenToFractal() {
  fractalopt = getOption("selectFractal3");
  iteropt = getOption("selectIter3");

  value = findFractalInSelect(fractalopt);

  data = [];
  msg = toMusicJson("", data, value, "music", iteropt.value, 25);
  sendMessage(msg);

  playsong();
}
function playsong() {
  msg = value + iteropt.value.toString();
  var audio = new Audio("./front-wav-files/" + msg + ".wav");
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
