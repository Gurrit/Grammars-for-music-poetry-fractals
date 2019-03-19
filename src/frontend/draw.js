const settings = {
  url: "ws://localhost:8765/",
  socket: null
};

function connectToServer() {
  let url = settings.url;
  var socket = new WebSocket(url);

  turtle = draw();
  socket.onmessage = function(event) {
    eval(event.data);
    console.log("EVENTDATA:" + event.data);
  };

  settings.socket = socket;
}

function draw() {
  canvas = document.getElementById("canvas1");
  let turtle = new CreateTurtle(canvas); // Needed for eval to work

  return turtle;
}

function sendMessage(message) {
  // message1 = JSON.stringify(message);
  settings.socket.send(message);
}
