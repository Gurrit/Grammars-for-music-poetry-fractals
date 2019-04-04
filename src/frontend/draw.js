const settings = {
    url:"ws://localhost:8765/",
    socket: null,
    drawer: null
};

function connectToServer() {
    let url = settings.url;
    var socket = new WebSocket(url);
    settings.drawer = new CreateDrawer(document.getElementById("canvas"));       // Needed for eval to wor
    let canvas = document.getElementById("canvas");// k
    let context = canvas.getContext('2d');
    socket.onmessage = function (event) {
        let dataStr = event.data;
        let [from, to] = dataStr.split(";");
        let coordinate1 = settings.drawer.extract(from);
        let coordinate2 = settings.drawer.extract(to);
        settings.drawer.draw(coordinate1, coordinate2);
    };
    return socket;
}

function sendMessage() {
    settings.socket.send("{\"type\":\"Sierpinski\", \n \"iteration\":7, \n \"step\":8 }");
}

function scale(factor) {
    settings.drawer.scale(0.5);
}

settings.socket = connectToServer();