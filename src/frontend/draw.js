const settings = {
    url:"ws://localhost:8765/",
    socket: null
};

function connectToServer() {
    let url = settings.url;
    var socket = new WebSocket(url);
    let turtle = new CreateTurtle(document.getElementById("canvas"));       // Needed for eval to work
    socket.onmessage = function (event) {
        console.log(event.data);
        eval(event.data)
    };
    return socket;
}

function sendMessage(message) {
    settings.socket.send("{\"type\":\"Koch\", \n \"iteration\":2, \n \"step\":3 }");
}

settings.socket = connectToServer();