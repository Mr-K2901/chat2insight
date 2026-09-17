const { createWhatsAppClient } = require('./client');
const { registerMessageListener } = require('./message_listener');

const client = createWhatsAppClient();
registerMessageListener(client);
client.initialize();
