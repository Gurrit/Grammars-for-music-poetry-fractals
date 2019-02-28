const settings = {
    url:"ws://localhost:8765/",
    socket: null
};

function connectToServer() {
    let url = settings.url;
    var socket = new WebSocket(url);
    console.log("Connected to server at " + url);
    let turtle = new CreateTurtle(document.getElementById("canvas"));
    turtle.forward(50);
    socket.onmessage = function (event) {
        console.log(event.data);
        eval("turtle." + event.data)
    }
    return socket;
}

function sendMessage(message) {
    settings.socket.send("hello");
}

settings.socket = connectToServer();