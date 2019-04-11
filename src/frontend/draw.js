const settings = {
  url: "ws://localhost:8765/",
  socket: null,
  drawers: []
};
a = 0;
function connectToServer(canvases) {
  let url = settings.url;
  let socket = new WebSocket(url);
  for (let canvas in canvases) {
    settings.drawers[canvas] = getTurtle(canvases[canvas].canvasen);
  }
  socket.onmessage = function(event) {
    let dataStr = event.data;
    console.log("DATAN TILL FRONTEND:" + event.data);
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
    socket.onmessage = function (event) {
        settings.drawers[1].reset();
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
        a++;
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
