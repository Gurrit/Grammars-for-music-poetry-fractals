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
        ev = event.data.split(",");
        for (let e in ev) {
            eval("settings." + ev[e]);
        }
        //console.log("EVENTDATA:" + event.data);
        //console.log("TURTLE:" + turtle);
    };

    settings.socket = socket;
}

function sendMessage(message) {
    settings.socket.send(message);
}
