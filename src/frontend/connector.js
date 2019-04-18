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
            console.log(message);
            drawNewFractal(message.lines, settings.drawers[message.canvas], message.type, message.iteration);
            break;
        case "music":
            setFileURL(message.content);
            break;
        case "translation":
            translateFractal(message.lines, settings.drawers[1], "#ff0017")
    }
}

function sendMessage(message) {
  console.log("sending messages" + message);
  settings.socket.send(message);
}

