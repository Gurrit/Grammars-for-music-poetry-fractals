globalStep = 25;
//fractalopt = "";
//iteropt = "";
//value = "";

function listenToFractal() {
  fractalopt = getOption("selectFractal3");
  iteropt = getOption("selectIter3");

  value = findFractalInSelect(fractalopt);

  msg1 = toMusicJson("", data, value, "music", iteropt.value, 25); //create the music file (wav and midi in backend)
  sendMessage(msg1);

  var x = 1;
  var y = null; // To keep under proper scope

  setTimeout(function() {
    x = x * 3 + 2;
    y = x / 2;
  }, 100);

  sendMessage(msg2);
  //playsong();
}

function setFileURL(eventdata) {
  objectURL = URL.createObjectURL(eventdata);
  console.log("Objecturl:" + objectURL.toString());

  playsong(objectURL);
}
function sendfiles() {
  data = [];

  fractalopt = getOption("selectFractal3");
  iteropt = getOption("selectIter3");

  value = findFractalInSelect(fractalopt);

  msg2 = toMusicJson("", data, value, "play", iteropt.value, 25);

  sendMessage(msg2);
}

function playsong(src) {
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

var xhr = new XMLHttpRequest();
xhr.open("GET", "/getFileName", true);
xhr.send();

xhr.onreadystatechange = function() {
  if (this.readyState == 4) {
    var filePath = this.responseText;
    var audio = document.getElementById("mySong");
    audio.src = filePath;
    audio.load();
    audio.oncanplaythrough = function() {
      this.play();
    };
  }
};
