function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('fileUrl').value = e.target.result;
        };
        reader.readAsDataURL(file);
    }
}

async function getSettings() {
    const idInstance = document.getElementById('idInstance').value;
    const apiTokenInstance = document.getElementById('apiTokenInstance').value;
    
    const response = await fetch('/api/getSettings', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ idInstance, apiTokenInstance })
    });
    await handleResponse(response);
}

async function getStateInstance() {
    const idInstance = document.getElementById('idInstance').value;
    const apiTokenInstance = document.getElementById('apiTokenInstance').value;
    
    const response = await fetch('/api/getStateInstance', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ idInstance, apiTokenInstance })
    });
    await handleResponse(response);
}

async function sendMessage() {
    const idInstance = document.getElementById('idInstance').value;
    const apiTokenInstance = document.getElementById('apiTokenInstance').value;
    const chatId = document.getElementById('chatId').value;
    const message = document.getElementById('message').value;
    
    const response = await fetch('/api/sendMessage', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ idInstance, apiTokenInstance, params: { chatId, message } })
    });
    await handleResponse(response);
}

async function sendFileByUrl() {
    const idInstance = document.getElementById('idInstance').value;
    const apiTokenInstance = document.getElementById('apiTokenInstance').value;
    const chatId = document.getElementById('chatId').value;
    const message = document.getElementById('message').value;
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (!file) {
        alert('Please select a file to send.');
        return;
    }

    const params = {
        chatId: chatId,
        urlFile: document.getElementById('fileUrl').value,
        fileName: file.name,
        caption: message
    };

    const response = await fetch('/api/sendFileByUrl', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ idInstance, apiTokenInstance, params })
    });
    await handleResponse(response);
}

async function handleResponse(response) {
    const responseText = await response.text();
    try {
        const data = JSON.parse(responseText);
        if (response.ok) {
            document.getElementById('responseField').textContent = JSON.stringify(data, null, 2);
        } else {
            document.getElementById('responseField').textContent = data.message;
        }
    } catch (e) {
        document.getElementById('responseField').textContent = 'Error parsing response';
    }
}
