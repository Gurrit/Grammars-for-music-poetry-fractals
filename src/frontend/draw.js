const settings = {
    url:"ws://localhost:8765/",
    socket: null
};

function connectToServer() {
    let url = settings.url;
    var socket = new WebSocket(url);
    let turtle = new CreateTurtle(document.getElementById("canvas"));       // Needed for eval to wor
    let canvas = document.getElementById("canvas");// k
    let context = canvas.getContext('2d');
    socket.onmessage = function (event) {
        let dataStr = event.data;
        let [from, to] = dataStr.split(";");
        let [fromX, fromY] = from.split(", ");
        let [toX, toY] = to.split(", ");
        let fromYNum = Number(fromY) + (canvas.width/2);
        let fromXNum = Number(fromX) + (canvas.width/2);
        let toYNum = Number(toY) + (canvas.width/2);
        let toXNum = Number(toX) + (canvas.width/2);
        context.moveTo(fromXNum, fromYNum);
        context.lineTo(toXNum, toYNum);
        context.stroke();
    };
    return socket;
}

function sendMessage(message) {
    settings.socket.send("{\"type\":\"Sierpinski\", \n \"iteration\":8, \n \"step\":8 }");
}

settings.socket = connectToServer();