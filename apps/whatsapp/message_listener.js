const axios = require('axios');

function registerMessageListener(client) {
  client.on('message', async (message) => {
    if (!message.body) return;
    await axios.post(`${process.env.WHATSAPP_API_URL || 'http://localhost:8000'}/messages`, {
      chat_id: message.from,
      sender: message.author || message.from,
      text: message.body,
      timestamp: new Date().toISOString(),
    });
  });
}

module.exports = { registerMessageListener };
