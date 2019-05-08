const settings = {
  url: "ws://192.168.99.100:8765",
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
    console.log(event.data);
    if (event.data instanceof Blob) {
      // Checks if type is of blob, then it is an image.
      setFileURL(event.data);
    }
    let message = JSON.parse(event.data);
    map_messages(message);
  };
  settings.socket = socket;
}

function map_messages(message) {
  switch (message.mode) {
    case "draw":
      drawNewFractal(
        message.lines,
        settings.drawers[message.canvas],
        message.type,
        message.iteration
      );
      break;
    case "translation":
      console.log(message);
      translateFractal(message.lines, settings.drawers[1], "#ff0017");
      break;
  }
}

function sendMessage(message) {
  settings.socket.send(message);
}
