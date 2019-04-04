const settings = {
    url: "ws://localhost:8765/",
    socket: null,
    turtles: []
};

function connectToServer(canvases) {
    let url = settings.url;
    let socket = new WebSocket(url);
    //borde vara turtle baserad på vilken canvas den ska utritas till (en if-sats)
    for (let canvas in canvases) {
        settings.turtles[canvas] = getTurtle(canvases[canvas].canvasen);
    }
    socket.onmessage = function (event) {
        let dataStr = event.data;
        let [from, to] = dataStr.split(";");
        let coordinate1 = settings.drawer.extract(from);
        let coordinate2 = settings.drawer.extract(to);
        settings.drawer.draw(coordinate1, coordinate2);
    };

    settings.socket = socket;
}

function sendMessage(message) {
  console.log("sending messages")
  settings.socket.send(message);
}

function scale(factor) {
    settings.drawer.scale(0.5);
}

settings.socket = connectToServer();