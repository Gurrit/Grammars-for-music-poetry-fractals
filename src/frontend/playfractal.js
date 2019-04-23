function setFileURL(eventdata) {
  //creates the URL for the sent wav file
  objectURL = URL.createObjectURL(eventdata);
  console.log("Objecturl:" + objectURL.toString());

  playsong(objectURL);
}
function sendfiles(id) {
  //send information av what fractal to generate and listen to
  data = [];

  if (id == "canv1play") {
    fractalopt = getOption("selectFractal1");
    iteropt = getOption("selectIter1");
    console.log("ID:" + id);
  } else {
    fractalopt = getOption("selectFractal2");
    iteropt = getOption("selectIter1");
  }

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
