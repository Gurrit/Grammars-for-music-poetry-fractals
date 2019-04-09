const settings = {
  url: "ws://localhost:8765/",
  socket: null,
  drawers: []
};

function connectToServer(canvases) {
  let url = settings.url;
  let socket = new WebSocket(url);
  //borde vara turtle baserad på vilken canvas den ska utritas till (en if-sats)
  console.log(canvases);
  for (let canvas in canvases) {
    settings.drawers[canvas] = getTurtle(canvases[canvas].canvasen);
  }
  socket.onmessage = function(event) {
    let dataStr = event.data;
    let [index, from, to, color] = dataStr.split(";");
    let coordinate1 = settings.drawers[index].extract(from);
    let coordinate2 = settings.drawers[index].extract(to);
    settings.drawers[index].color(color);
    settings.drawers[index].draw(coordinate1, coordinate2);

    console.log(event.data);
  };

  settings.socket = socket;
}

function sendMessage(message) {
  console.log("sending messages");
  array = settings.drawers;
  for (var i in array) {
    settings.drawers[i].reset();
  }
  console.log(settings.socket.send(message));
  settings.socket.send(message);
}

function scale(canvas, factor) {
  console.log("scaling");
  settings.drawers[canvas].scale(factor);
}
