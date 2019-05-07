canvplay = "";

function finishedLoadingBtn() {
  //for the "generete fractal"-button
  changetext(false);
  hideelement("loadingbar", "display");
}

function startedLoadingBtn() {
  //for the "generete fractal"-button
  changetext(true);
  showelement("loadingbar", "display");
}

function finishedmusic() {
  id = getCurrentPlay();
  showelement(id, "display");
  if (id == "canv2play") {
    hideelement("musicloading2", "display");
  } else if (id == "canv1play") {
    hideelement("musicloading1", "display");
  }
}

function hidemusic(id) {
  hideelement(id, "display");
  setCurrentPlay(id);
  console.log(id);
  if (id == "canv1play") {
    showelement("musicloading1", "display");
  } else if (id == "canv2play") {
    showelement("musicloading2", "display");
  }
}

function getCurrentPlay() {
  return canvplay;
}

function setCurrentPlay(id) {
  canvplay = id;
}
function hideelement(id, format) {
  //visbility for text, and display for divs and such
  var x = document.getElementById(id);

  if (format == "display") {
    x.style.display = "none";
  } else if (format == "visibility") {
    x.style.visbility = "hidden";
  }
}

function changetext(loading) {
  var btntext = document.getElementById("buttontext");

  if (loading) {
    btntext.innerText = "Loading";
  } else if (!loading) {
    btntext.innerText = "Generate Fractals";
  }
}

function showelement(id, format) {
  //visbility for text, and display for divs and such
  var x = document.getElementById(id);

  if (format == "display") {
    x.style.display = "inline-block";
  } else if (format == "visibility") {
    x.style.visbility = "initial";
  }
}
