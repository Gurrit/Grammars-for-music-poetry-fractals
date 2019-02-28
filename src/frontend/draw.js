const settings = {
    url:"ws://localhost:8765"
};

function connectToServer() {
    let url = settings.url;
    console.log(url);
    let socket = new WebSocket(url);
    socket.send("please connect me :)");
}

connectToServer(settings.url);