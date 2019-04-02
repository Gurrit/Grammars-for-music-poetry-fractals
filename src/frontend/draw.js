const settings = {
    url:"ws://localhost:8765/",
    socket: null
};

function connectToServer() {
    let url = settings.url;
    var socket = new WebSocket(url);
    let turtle = new CreateTurtle(document.getElementById("canvas"));       // Needed for eval to wor
    let context = document.getElementById("canvas").getContext("2d");// k
    let origX = 0;
    let origY = 0;
    socket.onmessage = function (event) {
        let dataStr = event.data;
        let [from, to] = dataStr.split(";");
        let [fromX, fromY] = from.split(", ");
        let [toX, toY] = to.split(", ");
        context.moveTo(fromX, fromY);
        context.lineTo(toX, toY);
        context.stroke();
    };
    return socket;
}

function sendMessage(message) {
    settings.socket.send("{\"type\":\"Sierpinski\", \n \"iteration\":2, \n \"step\":3 }");
}

settings.socket = connectToServer();