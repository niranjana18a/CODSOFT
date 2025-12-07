function sendMessage() {
    let inputField = document.getElementById("userInput");
    let userText = inputField.value.trim();

    if (userText === "") return;

    displayMessage(userText, "user-msg");
    inputField.value = "";

    fetch("/get", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: "msg=" + userText
    })
    .then(res => res.json())
    .then(data => {
        setTimeout(() => {
            displayMessage(data.response, "bot-msg");
        }, 400);
    });
}

function displayMessage(message, className) {
    let chatbox = document.getElementById("chatbox");

    let msgDiv = document.createElement("div");
    msgDiv.className = className;
    msgDiv.innerText = message;

    chatbox.appendChild(msgDiv);

    chatbox.scrollTop = chatbox.scrollHeight;
}

document.addEventListener("keypress", function(e){
    if(e.key === "Enter") sendMessage();
});
