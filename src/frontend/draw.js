const settings = {
  url: "ws://192.168.99.100:8765/",
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
    //setFileURL(event.data);

    typedArray = event.data;
    var blob = new Blob([typedArray.buffer], {
      type: "audio/wav"
    });

    console.log(event.data.toString());
    console.log(event.data.type);
    console.log(event.data.size);
    setFileURL(event.data);

    //var aBlob = new Blob(event.data, { type: "" });
    //console.log(aBlob);
    //let dataStr = event.data;

    //var reader = new FileReader();
    //reader.onload = function(e) {
    // The file's text will be printed here
    //console.log(e.target.result);
    //};

    //theFile = reader.readAsDataURL(file);

    //console.log(reader.readAsDataURL(file));

    //setFileURL(objectURL);

    //let datas = dataStr.split("|");
    //let len = datas.length - 1;
    //for (let data = 0; data < len; data++) {
    //  let [index, from, to, color] = datas[data].split(";");
    //  let coordinate1 = settings.drawers[index].extract(from);
    //  console.log("ska byta färg");
    //  settings.drawers[index].color(color);
    //  let coordinate2 = settings.drawers[index].extract(to);
    //  settings.drawers[index].saveNewLine(coordinate1, coordinate2);
    //}
    //let i = datas[len].substring(1, datas[len].length);
    //settings.drawers[i].scaleToSize();
    //settings.drawers[0].scaleToSize();
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
