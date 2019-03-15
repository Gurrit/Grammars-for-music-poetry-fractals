const settings = {
  url: "ws://localhost:8765/",
  socket: null
};

function connectToServer() {
  let url = settings.url;
  var socket = new WebSocket(url); //kmr inte längre än såhär
  console.log("kommer vi hit då?");
  console.log("The socket: " + socket);
  //let turtle = new CreateTurtle(document.getElementById("canvas1")); // Needed for eval to work
  socket.onmessage = function(event) {
    eval(event.data);
    console.log("EVENTET:" + event);
  };
  return socket;
}

function sendMessage(message) {
  // message1 = JSON.stringify(message);
  settings.socket.send(message);
}

settings.socket = connectToServer();
