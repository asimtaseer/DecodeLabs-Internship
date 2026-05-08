// ===== DOM Elements =====
const chatMessages = document.getElementById('chatMessages');
const messageInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const quickActions = document.getElementById('quickActions');

// Set welcome message time
document.getElementById('welcomeTime').textContent = formatTime(new Date());

// ===== Event Listeners =====
messageInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// ===== Functions =====
function formatTime(date) {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function sendQuickMessage(text) {
    messageInput.value = text;
    sendMessage();
}

async function sendMessage() {
    const text = messageInput.value.trim();
    if (!text) return;

    // Hide quick actions after first user message
    if (quickActions) {
        quickActions.style.display = 'none';
    }

    // Add user message
    appendMessage(text, 'user');
    messageInput.value = '';

    // Show typing indicator
    const typingEl = showTyping();

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });
        const data = await response.json();

        // Small delay for natural feel
        await delay(600 + Math.random() * 400);

        // Remove typing and show bot response
        typingEl.remove();
        appendMessage(data.response, 'bot');
    } catch (err) {
        typingEl.remove();
        appendMessage('Oops! Something went wrong. Please try again.', 'bot');
    }
}

function appendMessage(text, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${sender}-message`;

    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = sender === 'bot' ? '🤖' : '👤';

    const content = document.createElement('div');
    content.className = 'message-content';

    const bubble = document.createElement('div');
    bubble.className = 'message-bubble';
    bubble.textContent = text;

    const time = document.createElement('span');
    time.className = 'message-time';
    time.textContent = formatTime(new Date());

    content.appendChild(bubble);
    content.appendChild(time);
    msgDiv.appendChild(avatar);
    msgDiv.appendChild(content);

    chatMessages.appendChild(msgDiv);
    scrollToBottom();
}

function showTyping() {
    const typing = document.createElement('div');
    typing.className = 'typing-indicator';
    typing.innerHTML = `
        <div class="message-avatar">🤖</div>
        <div class="typing-dots">
            <span></span><span></span><span></span>
        </div>
    `;
    chatMessages.appendChild(typing);
    scrollToBottom();
    return typing;
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
