const settings = {
  url: "ws://192.168.99.100:8765/",
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
                settings.drawers[index].color(color);
                settings.drawers[index].saveNewLine(coordinate1, coordinate2);
        }
        let i = datas[len].substring(1, datas[len].length);
        settings.drawers[i].scaleToSize();
    };
    settings.socket = socket;

  }


function sendMessage(message) {
  console.log("sending messages");
  array = settings.drawers;
  //for (var i in array) {
    //settings.drawers[i].reset();
  //}

    settings.drawers[0].reset();
  console.log(settings.socket.send(message));
  settings.socket.send(message);
}

function scale(canvas, factor) {
  console.log("scaling");
  settings.drawers[canvas].scale(factor);
}



