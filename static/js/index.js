// Common base JS for handling messages
const MessageHandler = {
    showMessage: function (type, message) {
        const messageContainer = document.createElement('div');
        messageContainer.className = `message ${type}`;
        messageContainer.textContent = message;

        document.body.appendChild(messageContainer);

        // Automatically remove the message after 3 seconds
        setTimeout(() => {
            messageContainer.remove();
        }, 3000);
    }
};

// Use case example
document.addEventListener('DOMContentLoaded', () => {
    // Show a success message
    MessageHandler.showMessage('success', 'Operation completed successfully!');

    // Show an error message
    MessageHandler.showMessage('error', 'An error occurred while processing your request.');
});