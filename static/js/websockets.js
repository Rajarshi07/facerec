const roomName = JSON.parse(document.getElementById('session-name').textContent);
if (location.protocol === 'https:') {
    var protocol = 'wss://'
}
else {
    var protocol = 'ws://'
}
var chatSocket;
function connect() {
    chatSocket = new WebSocket(
        protocol
        + window.location.host
        + '/ws/reports/'
        + roomName
        + '/'
    );

    chatSocket.onopen = function (e) {
        console.log('Chat socket connected successfully');
    }

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        console.log("ON_MESSAGE",data)
    };

    chatSocket.onclose = function (e) {
        console.error('Chat socket closed unexpectedly...reconnecting');
        
        let timerInterval;
        var interval = setTimeout(function () {
            connect();
        }, 3000);
    };
}

connect();

async function sendData(msg){
    data = {}
    data['message'] = JSON.stringify(msg);
    chatSocket.send(JSON.stringify(data));
}
