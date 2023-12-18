// main.js
function sendMessage() {
    let userInput = document.getElementById('user-input').value;
    document.getElementById('chat-box').innerHTML += `<p>User: ${userInput}</p>`;
    document.getElementById('user-input').value = '';

    $.ajax({
        type: 'POST',
        url: '/chat',
        data: { user_input: userInput },
        success: function (data) {
            let botResponse = data.response;
            document.getElementById('chat-box').innerHTML += `<p>Bot: ${botResponse}</p>`;
        }
    });
}
