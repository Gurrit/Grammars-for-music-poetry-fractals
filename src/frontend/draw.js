const settings = {
    url:"ws://localhost:8765/",
    socket: null
};

function connectToServer() {
    let url = settings.url;
    var socket = new WebSocket(url);
    console.log("Connected to server at " + url);
    return socket;
}

function sendMessage(message) {
    settings.socket.send("hello");
}

settings.socket = connectToServer();