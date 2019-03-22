const settings = {
  url: "ws://localhost:8765/",
  socket: null
};

function connectToServer() {
  let url = settings.url;
  var socket = new WebSocket(url);

  //borde vara turtle baserad på vilken canvas den ska utritas till (en if-sats)
  turtle = getTurtle("canvas1");

  socket.onmessage = function(event) {
    eval(event.data);
    //console.log("EVENTDATA:" + event.data);
    //console.log("TURTLE:" + turtle);
  };

  settings.socket = socket;
}

function sendMessage(message) {
  settings.socket.send(message);
}
