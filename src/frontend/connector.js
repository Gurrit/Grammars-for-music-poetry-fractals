const settings = {
  url: "ws://localhost:8765",
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
    if (event.data instanceof Blob) {
      // Checks if type is of blob, then it is an image.
      setFileURL(event.data);
      return;
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
        message.iteration,
        message.modified
      );
      break;
    case "translation":
      translateFractal(message.lines,
          settings.drawers[message.canvas],
          "#ff0017");
      break;
  }
}

function sendMessage(message) {
  settings.socket.send(message);
}
