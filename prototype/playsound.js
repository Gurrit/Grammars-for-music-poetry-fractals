window.addEventListener("keydown", function(e) {
  console.log("test");
});

var idList = [];

function play(id) {
  console.log("Funkar att trycka iaf :" + id);

  var audio = document.getElementById(id);
  console.log(audio.play());
  audio.play();

  idList.push(id + ",");
  console.log(idList);

  for (i in idList) {
    if (i == 0) {
      var string = idList[i];
    } else {
      var string = string + idList[i];
    }
    i++;
  }
  document.getElementById("noteID").value = string;
}
