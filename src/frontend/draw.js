const settings = {
  url: "ws://192.168.99.100:8765/",
  socket: null,
  drawers: []
};

function connectToServer(canvases) {
  let url = settings.url;
  let socket = new WebSocket(url);
  for (let canvas in canvases) {
    settings.drawers[canvas] = getTurtle(canvases[canvas].canvasen);
  }
  socket.onmessage = function(event) {
    let dataStr = event.data;

    console.log(event.data);
    if (event.data[0] == "0" || event.data[0] == "1") {
      console.log("drawing mode");
      let datas = dataStr.split("|");

      let len = datas.length - 1;
      for (let data = 0; data < len; data++) {
        let [index, from, to, color] = datas[data].split(";");
        let coordinate1 = settings.drawers[index].extract(from);
        console.log("ska byta färg");
        settings.drawers[index].color(color);
        let coordinate2 = settings.drawers[index].extract(to);
        settings.drawers[index].saveNewLine(coordinate1, coordinate2);
      }
      let i = datas[len].substring(1, datas[len].length);
      //settings.drawers[i].scaleToSize();
      settings.drawers[0].scaleToSize();
    } else {
      console.log("playing mode");
      setFileURL(event.data);
    }
  };

  settings.socket = socket;
}

function sendMessage(message) {
  console.log("sending messages");
  array = settings.drawers;
  for (var i in array) {
    settings.drawers[i].reset();
  }
  settings.socket.send(message);
}

function scale(canvas, factor) {
  console.log("scaling");
  settings.drawers[canvas].scale(factor);
}
