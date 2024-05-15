/* Front-end code created using AI */
const init_promptInput = document.getElementById('initial-prompt');
const sendButton = document.getElementById('send-prompt-btn');

const inputContainer = document.getElementById('input-container');

const responseContainer = document.getElementById('response-container');
const responseContent = responseContainer.querySelector('.response-content');
const promptContentInResponse = responseContainer.querySelector('.prompt-content');

const promptContainer = document.getElementById('prompt-container');
const promptContent = promptContainer.querySelector('.prompt-content');

const loader = document.querySelector('.loader');


// Function to automatically adjust the height of the textarea
function autoResizeTextarea() {
    this.style.height = 'auto';
    this.style.height = `${this.scrollHeight}px`;
}

// Attach the autoResizeTextarea function to the input event of the textarea
init_promptInput.addEventListener('input', autoResizeTextarea);

// Add event listener to the Send Prompt button
sendButton.addEventListener('click', sendPrompt);

function sendPrompt() {
    promptContainer.style.display = "block";
    inputContainer.style.display = "none";
    const prompt = init_promptInput.value.trim();
    if (prompt) {
        promptContent.textContent = prompt;
        sendPromptToServer(prompt);
    } else {
        alert('Please enter a prompt before sending.');
    }
}

function sendPromptToServer(prompt) {
    const url = 'http://localhost:5000/get_response';
    const data = { prompt };

    loader.style.display = 'block'; // Show the loading spinner

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        responseContainer.style.display = "block";
        promptContainer.style.display = "none";
        loader.style.display = 'none';
        promptContentInResponse.textContent = prompt;
        responseContent.textContent = data.response_from_server;
    })
    .catch(error => {
        console.error('Error:', error);
        loader.style.display = 'none'; // Hide the loading spinner
    });
}