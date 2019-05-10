canvplay = "";

function finishedLoadingBtn() {
  //for the "generete fractal"-button
  changetext(false);
  hideElement("loadingbar", "display");
}

function startedLoadingBtn() {
  //for the "generete fractal"-button
  changetext(true);
  showelement("loadingbar", "display");
}

function finishedmusic() {
  id = getCurrentPlay();
  showelement(id, "display");
  if (id === "canv2play") {
    hideElement("musicloading2", "display");
  } else if (id === "canv1play") {
    hideElement("musicloading1", "display");
  }
}

function hidemusic(id) {
  hideElement(id, "display");
  setCurrentPlay(id);
  if (id === "canv1play") {
    showelement("musicloading1", "display");
  } else if (id === "canv2play") {
    showelement("musicloading2", "display");
  }
}

function getCurrentPlay() {
  return canvplay;
}

function setCurrentPlay(id) {
  canvplay = id;
}
function hideElement(id, format) {
  //visbility for text, and display for divs and such
  let x = document.getElementById(id);

  if (format === "display") {
    x.style.display = "none";
  } else if (format === "visibility") {
    x.style.visbility = "hidden";
  }
}

function changetext(loading) {
  let btntext = document.getElementById("buttontext");

  if (loading) {
    btntext.innerText = "Loading";
  } else if (!loading) {
    btntext.innerText = "Generate Fractals";
  }
}

function showelement(id, format) {
  //visbility for text, and display for divs and such
  let x = document.getElementById(id);

  if (format === "display") {
    x.style.display = "inline-block";
  } else if (format === "visibility") {
    x.style.visbility = "initial";
  }
}

function showorhidepic() {
  let helpimage = document.getElementById("pianohelp");
  if (helpimage.style.display === "inline-block") {
    hideElement("pianohelp", "display");
  } else {
    showelement("pianohelp", "display");
  }
}
