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
   /*   if(settings.hasRun < 2) {
          settings.drawers[1].reset();
      }
      else {
          settings.drawers[1].drawings = [];
          settings.drawers[1].strokeWidth = 1;
          settings.drawers[1].strokeStyle = "#000000";
          settings.drawers[1].redraw();
      }
    let dataStr = event.data;
    let datas = dataStr.split("|");
    let len = datas.length - 1;
    for (let data = 0; data < len; data++) {
        let [index, from, to, color] = datas[data].split(";");
        let coordinate1 = settings.drawers[index].extract(from);
        settings.drawers[index].color(color);
        let coordinate2 = settings.drawers[index].extract(to);
        settings.drawers[index].saveNewLine(coordinate1, coordinate2);
        if(settings.hasRun >=2 ) {
            settings.drawers[index].draw(coordinate1, coordinate2);
        }
    }
        let [_, meta] = datas[len].split("+");
        let [i, frac] = meta.split("&");
        if(settings.hasRun < 2) {       // Once again, bad code.
          settings.drawers[i].scaleToSize();
        let [type, iter] = frac.split("*");
            settings.drawers[i].saveFractal(type, iter);
            settings.hasRun++
        }
        else {
            settings.drawers[i].penWidth = 3;
            settings.drawers[i].color("#ff0000");
            settings.drawers[i].redraw();
        }*/
    };

    settings.socket = socket;
}

function map_messages(message) {
    switch(message.mode) {
        case "draw":
            drawNewFractal(message.lines, settings.drawers[message.canvas]);
            break;
        case "music":
            setFileURL(message.content)
    }

}

function sendMessage(message) {
  console.log("sending messages");
  settings.socket.send(message);
}

