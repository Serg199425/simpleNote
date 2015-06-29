socket_connect();
friends_invitations_count = 0;
unreaded_notes_count = 0;
groups_invitations_count = 0;

function socket_connect() {
    socket = new SockJS('http://' + 'localhost' + ':8989/update_notifications');  // ваш порт для асинхронного сервиса
    // при соединении вызываем событие login, которое будет выполнено на серверной стороне

    socket.onmessage = function(msg){
        window['ws_order_update_notifications'](msg.data);  // роутер, выполняет функцию согласно типу сообщения
    }

    socket.onclose = function(e){
        setTimeout(socket_connect, 5000);
    };
}

function ws_order_update_notifications(msg){
    console.log(msg);
    change_friends_count(msg);
    change_unreaded_notes_count(msg);
    change_groups_invitations_count(msg);
}