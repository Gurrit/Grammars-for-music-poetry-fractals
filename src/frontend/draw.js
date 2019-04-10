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
    socket.onmessage = function (event) {
        let dataStr = event.data;
        let datas = dataStr.split("|");
        let len = datas.length - 1;
        for (let data = 0; data < len ; data++) {
                let [index, from, to] = datas[data].split(";");
                let coordinate1 = settings.drawers[index].extract(from);
                let coordinate2 = settings.drawers[index].extract(to);
                settings.drawers[index].saveNewLine(coordinate1, coordinate2);
        }
        let [_, meta] = datas[len].split("+");
        let [i, frac] = meta.split("&");
        settings.drawers[i].scaleToSize();
        let [type, iter] = frac.split("*");
        settings.drawers[i].saveFractal(type, iter);
    };

    settings.socket = socket;
}

function sendMessage(message) {
  console.log("sending messages");
  settings.socket.send(message);
}