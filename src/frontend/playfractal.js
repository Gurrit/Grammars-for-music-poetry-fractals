function setFileURL(eventdata) {
  //creates the URL for the sent wav file
  objectURL = URL.createObjectURL(eventdata);
  console.log("Objecturl:" + objectURL.toString());

  playsong(objectURL);
}
function sendfiles(id) {
  //send information av what fractal to generate and listen to

  if (id == "canv1play") {
    fractalopt = getOption("selectFractal1");
    iteropt = getOption("selectIter1");
    data = getOption("selectScale1");
  } else {
    fractalopt = getOption("selectFractal2");
    iteropt = getOption("selectIter1");
    data = getOption("selectScale2");
  }

  value = findFractalInSelect(fractalopt);

  if (value === "") {
    alert("You have not selected a fractal to play.");
    return;
  }

  console.log(iteropt.value);
  if (iteropt.value == "Select iteration") {
    alert("You have not selected an iteration.");
    return;
  }

  console.log("Skalan: " + data.value);

  msg = toJson(0, data.value, value, "play", iteropt.value);

  sendMessage(msg);
}

function playsong(src) {
  //play the song
  console.log(src);
  var audio = new Audio(src);
  audio.play();
}
