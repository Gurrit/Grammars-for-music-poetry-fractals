const settings = {
  url: "ws://localhost:8765/",
  socket: null,
  drawers: [],
  hasRun: 0
};

function connectToServer(canvases) {
  let url = settings.url;
  let socket = new WebSocket(url);
  for (let canvas in canvases) {
    settings.drawers[canvas] = getTurtle(canvases[canvas].canvasen);
  }
  socket.onmessage = function(event) {
      let message = JSON.parse(event.data);
      map_messages(message);
    };
    settings.socket = socket;
}

function map_messages(message) {
    switch(message.mode) {
        case "draw":
            drawNewFractal(message.lines, settings.drawers[message.canvas], message.type, message.iteration);
            break;
        case "music":
            setFileURL(message.content);
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

